# create_sample_data.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/cstresto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Category, MenuItem, OrderStatus, Order, OrderItem, Transaction

# Create some sample data
def create_sample_data():
    # Create categories
    food_category = Category(name='Food')
    beverage_category = Category(name='Beverage')

    db.session.add_all([food_category, beverage_category])
    db.session.commit()

    # Create menu items
    item1 = MenuItem(name='Burger', price=10.99, category=food_category)
    item2 = MenuItem(name='Pizza', price=12.99, category=food_category)
    item3 = MenuItem(name='Soda', price=2.99, category=beverage_category)

    db.session.add_all([item1, item2, item3])
    db.session.commit()

    # Create order status
    open_status = OrderStatus(status='Open')
    invoiced_status = OrderStatus(status='Invoiced')

    db.session.add_all([open_status, invoiced_status])
    db.session.commit()

    # Create an order with items
    order = Order(table_number=1, created_at=datetime.utcnow(), total_amount=25.97, status=open_status)

    order_item1 = OrderItem(order=order, menu_item=item1, quantity=2, subtotal=2 * item1.price)
    order_item2 = OrderItem(order=order, menu_item=item3, quantity=1, subtotal=item3.price)

    db.session.add_all([order, order_item1, order_item2])
    db.session.commit()

    # Create a transaction for the order
    transaction = Transaction(order=order, payment_method='Credit Card', amount_paid=25.97)

    db.session.add(transaction)
    db.session.commit()

if __name__ == '__main__':
    create_sample_data()
