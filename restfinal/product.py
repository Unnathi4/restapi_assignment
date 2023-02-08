from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db
db = SQLAlchemy(app)
app.app_context().push()

ma = Marshmallow(app)


class products(db.Model):
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(100), unique=True)
    SupplierID = db.Column(db.Integer)
    CategoryID = db.Column(db.Integer)
    QuantityPerUnit = db.Column(db.String(100))
    UnitPrice = db.Column(db.Float)
    UnitsInStock = db.Column(db.Integer)
    UnitsOnOrder = db.Column(db.Integer)
    ReorderLevel = db.Column(db.Integer)
    Discontinued = db.Column(db.Integer)

    def __init__(self, ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock,
                 UnitsOnOrder, ReorderLevel, Discontinued):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.SupplierID = SupplierID
        self.CategoryID = CategoryID
        self.QuantityPerUnit = QuantityPerUnit
        self.UnitPrice = UnitPrice
        self.UnitsInStock = UnitsInStock
        self.UnitsOnOrder = UnitsOnOrder
        self.ReorderLevel = ReorderLevel
        self.Discontinued = Discontinued


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('ProductID', 'ProductName', 'SupplierID', 'CategoryID', 'QuantityPerUnit', 'UnitPrice', 'UnitsInStock','UnitsOnOrder', 'ReorderLevel', 'Discontinued')


Product_schema = ProductSchema()
Products_schema = ProductSchema(many=True)


# Create a Product
@app.route('/productadd', methods=['POST'])
def add_customer():
    ProductID = request.json['ProductID']
    ProductName = request.json['ProductName']
    SupplierID = request.json['SupplierID']
    CategoryID = request.json['CategoryID']
    QuantityPerUnit = request.json['QuantityPerUnit']
    UnitPrice = request.json['UnitPrice']
    UnitsInStock = request.json['UnitsInStock']
    UnitsOnOrder = request.json['UnitsOnOrder']
    ReorderLevel = request.json['ReorderLevel']
    Discontinued = request.json['Discontinued']

    new_product = products(ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock,
                           UnitsOnOrder, ReorderLevel, Discontinued)

    db.session.add(new_product)
    db.session.commit()

    return Product_schema.jsonify(new_product)


@app.route('/productall', methods=['GET'])
def get_products():
    all_products = products.query.all()
    result = Products_schema.dump(all_products)
    return jsonify(result)



@app.route('/product/<ProductID>', methods=['GET'])
def get_product(ProductID):
    product = products.query.get(ProductID)
    return Product_schema.jsonify(product)


@app.route('/updateproduct/<ProductID>', methods=['PUT'])
def update_product(ProductID):
    product = products.query.get(ProductID)

    ProductID = request.json['ProductID']
    ProductName = request.json['ProductName']
    CategoryID = request.json['CategoryID']
    UnitsOnOrder = request.json['UnitsOnOrder']
    Discontinued = request.json['Discontinued']

    product.ProductID = ProductID
    product.ProductName = ProductName
    product.CategoryID = CategoryID
    product.UnitsOnOrder = UnitsOnOrder
    product.Discontinued = Discontinued

    db.session.commit()

    return Product_schema.jsonify(product)


if __name__ == '__main__':
    app.run(port=5001)