from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
# from models import Category, MenuItem, OrderStatus, Order, OrderItem, Transaction

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/cstresto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app, resources={r"/*":{'origins':"*"}})
# CORS(app, resources={r'/*':{'origins': 'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})
# app.config.from_object(__name__)
migrate = Migrate(app, db)

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class MenuItem(db.Model):
    __tablename__ = 'menu_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    image = db.Column(db.String(255))

class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)
    total_amount = db.Column(db.Integer, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)

class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)

class InvoiceDetail(db.Model):
    __tablename__ = 'invoice_detail'
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Integer, nullable=False)

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    amount_paid = db.Column(db.Integer, nullable=False)

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
        menu_items = MenuItem.query.all()
        response_object['menu_items'] = [{'id': item.id, 'name': item.name, 'price': item.price, 'category_id': item.category_id, 'image': item.image} for item in menu_items]

    return jsonify(response_object)

# return all menu
@app.route('/menu_items/<int:item_id>', methods=['PUT', 'DELETE'])
def single_menu_item(item_id):
    response_object = {'status': 'success'}
    menu_item = MenuItem.query.get(item_id)

    if request.method == 'PUT':
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

# route to fetch categories
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    category_list = [
        {
            'id': category.category_id,
            'name': category.name
        }
        for category in categories
    ]
    return jsonify({'categories': category_list})


if __name__ == "__main__":
    app.run(debug=True)