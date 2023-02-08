from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/crud'
db = SQLAlchemy(app)
app.app_context().push()
ma = Marshmallow(app)

class Customers(db.Model):

    CustomerID = db.Column(db.String(100),primary_key=True)
    CompanyName = db.Column(db.String(100))
    ContactName = db.Column(db.String(200))
    ContactTitle = db.Column(db.String(100))
    Address = db.Column(db.String(100))
    City = db.Column(db.String(100))
    Region = db.Column(db.String(100))
    PostalCode = db.Column(db.String(100))
    Country = db.Column(db.String(100))
    Phone = db.Column(db.String(100))
    Fax = db.Column(db.String(100))

    def __init__(self, CustomerID,CompanyName,ContactName,ContactTitle,Address,City,Region,PostalCode,Country,Phone,Fax):
        self.CustomerID = CustomerID
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax

class CustomerSchema(ma.Schema):

    class Meta:

      fields = ('CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax')

Customer_schema = CustomerSchema()
Customers_schema = CustomerSchema(many=True)

@app.route('/addcustomer', methods=['POST'])
def add_customer():
    CustomerID = request.json['CustomerID']
    CompanyName = request.json['CompanyName']
    ContactName = request.json['ContactName']
    ContactTitle = request.json['ContactTitle']
    Address = request.json['Address']
    City = request.json['City']
    Region = request.json['Region']
    PostalCode = request.json['PostalCode']
    Country = request.json['Country']
    Phone = request.json['Phone']
    Fax = request.json['Fax']





    new_customer = Customers(CustomerID,CompanyName,ContactName,ContactTitle,Address,City,Region,PostalCode,Country,Phone,Fax)

    db.session.add(new_customer)
    db.session.commit()

    return Customer_schema.jsonify(new_customer)

@app.route('/allcustomer',methods=['GET'])
def get_customers():
  all_customers = Customers.query.all()
  result = Customers_schema.dump(all_customers)
  return jsonify(result)

@app.route('/customer/<CustomerID>', methods=['GET'])
def get_customer(CustomerID):
  customer = Customers.query.get(CustomerID)
  return Customer_schema.jsonify(customer)

@app.route('/updatecustomer/<CustomerID>', methods=['PUT'])
def update_customer(CustomerID):
  customer = Customers.query.get(CustomerID)
  ContactName = request.json['ContactName']
  ContactTitle = request.json['ContactTitle']
  Phone = request.json['Phone']

  customer.ContactName = ContactName
  customer.ContactTitle = ContactTitle
  customer.Phone = Phone

  db.session.commit()

  return Customer_schema.jsonify(customer)


if __name__ == "__main__":
    app.run(debug=True)