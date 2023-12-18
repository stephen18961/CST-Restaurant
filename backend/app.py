from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from models import *

###########################################################################################################
# ROUTES -------------------------------------------------------------------------------------------------#
###########################################################################################################
@app.route('/')
def hello():
    return("Hello World!")

@app.route('/hello', methods=['GET'])
def greetings():
    return("Hello, world! HELLO HELLO")

# Menu Items Route Handlers
@app.route('/menu_items', methods=['GET', 'POST'])
def menu_items():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data = request.json
        new_menu_item = MenuItem(name=data['name'], price=data['price'], category_id=data['category_id'], image=data.get('image'))
        db.session.add(new_menu_item)
        db.session.commit()
        response_object['message'] = 'Menu item added successfully'
        response_object['id'] = new_menu_item.id
    else:   
        category_id = request.args.get('category_id')

        if category_id:
            # Filter menu items by category_id
            menu_items = MenuItem.query.filter_by(category_id=category_id).all()
        else:
            # Retrieve all menu items if no category_id is provided
            menu_items = MenuItem.query.all()

        response_object['menu_items'] = [
            {'id': item.id, 'name': item.name, 'price': item.price, 'category_id': item.category_id, 'image': item.image}
            for item in menu_items
        ]

    return jsonify(response_object)

# return menu by id
@app.route('/menu_items/<int:item_id>', methods=['PUT', 'DELETE', 'POST', 'GET'])
def single_menu_item(item_id):
    response_object = {'status': 'success'}
    menu_item = MenuItem.query.get(item_id)
    
    if request.method == 'GET':
        if menu_item:
            response_object['menu_item'] = {
                'id': menu_item.id,
                'name': menu_item.name,
                'price': menu_item.price,
                'category_id': menu_item.category_id,
                'image': menu_item.image,
                # Add other fields as needed
            }
        else:
            response_object['error'] = 'Menu item not found'
    elif request.method == 'PUT':
        if menu_item:
            data = request.json
            menu_item.name = data['name']
            menu_item.price = data['price']
            menu_item.category_id = data['category_id']
            menu_item.image = data.get('image')
            db.session.commit()
            response_object['message'] = 'Menu item updated successfully'
        else:
            response_object['error'] = 'Menu item not found'
    elif request.method == 'DELETE':
        if menu_item:
            db.session.delete(menu_item)
            db.session.commit()
            response_object['message'] = 'Menu item deleted successfully'
        else:
            response_object['error'] = 'Menu item not found'

    return jsonify(response_object)

# ability to show images
@app.route('/static/images/<path:filename>')
def serve_static(filename):
    return send_from_directory('static/images', filename)

# route for fetching category
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    categories_list = [{'category_id': category.category_id, 'name': category.name} for category in categories]
    return jsonify({'categories': categories_list})

# route for tables
@app.route('/tables', methods=['GET'])
def get_tables():
    tables = TableStatus.query.all()
    tables_list = [{'table_id' : table.id, 'occupied': False if table.occupied == 0 else True} for table in tables]
    return jsonify({'tables_list': tables_list})

# route for posting order
@app.route('/order', methods=['POST'])
def post_order():
    if request.method == 'POST':
        data = request.json
        inv_data = data['invoiceData']

        table_status = TableStatus.query.get(inv_data['table_number'])
        table_status.occupied = 1
        db.session.commit()
        
        new_invoice = Invoice(table_number=inv_data['table_number'], created_at=datetime.now(), total_amount=inv_data['total_amount'], status_id=inv_data['status_id'])
        db.session.add(new_invoice)
        db.session.commit()

        invoice_idd = db.session.query(Invoice.id).order_by(Invoice.id.desc()).first()
        invoice_idd = int(invoice_idd[0])

        inv_detail = data['invoiceDetailData']
        n_items = len(inv_detail)

        for i in range(n_items):
            new_invoice_detail = InvoiceDetail(invoice_id=invoice_idd, menu_item_id=inv_detail[i]['menu_item_id'])
            db.session.add(new_invoice_detail)

        db.session.commit()

    return ('Successfully added to database :DDDDD')

@app.route('/invoices', methods=['GET'])
def get_invoices():
    invoices = Invoice.query.all()
    invoices_list = []

    for invoice in invoices:
        status = Status.query.get(invoice.status_id)
        status_data = {
            'id': status.id,
            'status': status.status
        }

        invoice_data = {
            'id': invoice.id,
            'table_number': invoice.table_number,
            'created_at': invoice.created_at.isoformat(),
            'total_amount': invoice.total_amount,
            'status': status_data  # Include status information in the invoice_data
        }
        invoices_list.append(invoice_data)
    return jsonify({'invoices': invoices_list})

# Route to fetch invoice details based on invoice ID
@app.route('/invoices/<int:invoice_id>/details', methods=['GET'])
def get_invoice_details(invoice_id):
    invoice_details = InvoiceDetail.query.filter_by(invoice_id=invoice_id).all()

    if not invoice_details:
        return jsonify({'message': 'No details found for the given invoice ID'}), 404

    details_list = []
    for detail in invoice_details:
        menu_item = MenuItem.query.get(detail.menu_item_id)
        menu_data = {
            'id': menu_item.id,
            'name': menu_item.name,
            'price': menu_item.price,
            'category_id': menu_item.category_id,
            'image': menu_item.image
        }

        detail_data = {
            'id': detail.id,
            'invoice_id': detail.invoice_id,
            'menu_item': menu_data,
        }
        details_list.append(detail_data)
        print(details_list)
    return jsonify({'invoice_details': details_list})

# Route to fetch an invoice based on invoice ID
@app.route('/invoices/<int:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    try:
        invoice = Invoice.query.filter_by(id=invoice_id).first()

        if not invoice:
            return jsonify({'message': 'Invoice not found'}), 404

        invoice_data = {
            'id': invoice.id,
            'table_number': invoice.table_number,
            'created_at': invoice.created_at.isoformat(),
            'total_amount': invoice.total_amount,
            'status_id': invoice.status_id
        }
        return jsonify({'invoice': invoice_data})

    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
# Menu Items Route Handlers
@app.route('/finish_payment', methods=['POST'])
def finish_payment():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        invoice_id = request.json['invoice_id']

        # Alter Invoice Status
        invoice = Invoice.query.filter_by(id=invoice_id).first()
        invoice.status_id = 3

        # Alter Table Status
        table_number = invoice.table_number
        table = TableStatus.query.filter_by(id=table_number).first()
        table.occupied = 0

        # Add new transaction
        new_transaction = Transaction(invoice_id=invoice_id, payment_method='CASH', amount_paid=invoice.total_amount)
        db.session.add(new_transaction)

        # Commit action!
        db.session.commit()
        response_object['message'] = 'Transaction done.'

    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)