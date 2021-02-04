from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, json
from marshmallow import fields, validate
from marshmallow_sqlalchemy import ModelSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Creating Model
class Customers(db.Model):
    __tablename__ = 'customers'

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    customerId = db.Column(db.String(5), primary_key=True)
    companyName = db.Column(db.String(40), nullable=False)
    contactName = db.Column(db.String(30), nullable=False)
    contactTitle = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    region = db.Column(db.String(15), nullable=False)
    postalCode = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(24), nullable=False)
    fax = db.Column(db.String(24), nullable=False)


class Products(db.Model):
    __tablename__= 'products'

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    productId = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(40), nullable=False)
    supplierId = db.Column(db.Integer, nullable=False)
    categoryId = db.Column(db.Integer, nullable=False)
    quantityPerUnit = db.Column(db.String(20), nullable=False)
    unitPrice = db.Column(db.Float, nullable=False)
    unitsInStock = db.Column(db.Integer, nullable=False)
    unitsOnOrder = db.Column(db.Integer, nullable=False)
    reorderLevel = db.Column(db.Integer, nullable=False)
    discontinued = db.Column(db.Integer, nullable=False)



class Orders(db.Model):
    __tablename__ = 'orders'

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    orderId = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.String(5), nullable=False)
    employeeId = db.Column(db.Integer, nullable=False)
    orderDate = db.Column(db.DateTime, nullable=False)
    requiredDate = db.Column(db.DateTime, nullable=False)
    shippedDate = db.Column(db.DateTime, nullable=False)
    shipVia = db.Column(db.Integer, nullable=False)
    freight = db.Column(db.Float, nullable=False)
    shipName = db.Column(db.String(40), nullable=False)
    shipAddress = db.Column(db.String(60), nullable=False)
    shipCity = db.Column(db.String(15), nullable=False)
    shipRegion = db.Column(db.String(15), nullable=False)
    shipPostalCode = db.Column(db.String(10), nullable=False)
    shipCountry = db.Column(db.String(15), nullable=False)


class Categories(db.Model):
    __tablename__ = 'categories'
    categoryId = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(50), nullable=False)


# Creating Schemas
class OrderSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        sqla_session = db.session

    orderId = fields.Integer()
    customerId = fields.Str()
    employeeId = fields.Integer()
    orderDate = fields.DateTime()
    requiredDate = fields.DateTime()
    shippedDate = fields.DateTime()
    shipVia = fields.Integer()
    freight = fields.Float(default=0)
    shipName = fields.Str()
    shipAddress = fields.Str()
    shipCity = fields.Str()
    shipRegion = fields.Str()
    shipPostalCode = fields.Str()
    shipCountry = fields.Str()


class CustomerSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Customers
        sqla_session = db.session

    customerId = fields.Str(validate=validate.Length(min=5, max=5))
    companyName = fields.Str()
    contactName = fields.Str()
    contactTitle = fields.Str()
    address = fields.Str()
    city = fields.Str()
    region = fields.Str()
    postalCode = fields.Str()
    country = fields.Str()
    phone = fields.Str(validate=validate.Length(min=10,max =10))
    fax = fields.Str()


class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Products
        sqla_session = db.session

    productId = fields.Integer()
    productName = fields.Str()
    supplierId = fields.Integer()
    categoryId = fields.Integer()
    quantityPerUnit = fields.Str()
    unitPrice = fields.Float(default=0)
    unitsInStock = fields.Integer()
    unitsOnOrder = fields.Integer()
    reorderLevel = fields.Integer()
    discontinued = fields.Integer()


@app.route("/insert_customer", methods=["POST"])
def insert_customer():
    try:
        data = request.get_json()
        if Customers.query.filter_by(customerId=data['customerId']).first():
            return jsonify({'status': "data already present"})
        else:
            customer_schema = CustomerSchema()
            customer = customer_schema.load(data)
            result = customer_schema.dump(customer.create())
            return jsonify({'status': result})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/insert_product', methods=['POST'])
def insert_product():
    try:
        data = request.get_json()
        if Products.query.filter_by(productId=data['productId']).first():
            return jsonify({'status': "data already present"})
        else:
            product_schema = ProductSchema()
            product = product_schema.load(data)
            result = product_schema.dump(product.create())
            return jsonify({'status': result})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/insert_order', methods=['POST'])
def insert_orders():
    try:
        data = request.get_json()
        if Orders.query.filter_by(orderId=data['orderId']).first():
            return jsonify({'status': "data already present"})
        else:
            order_schema = OrderSchema()
            order = order_schema.load(data)
            result = order_schema.dump(order.create())
            return jsonify({'status': result})
    except Exception as e:
        return jsonify({'error': str(e)})

# Updation of customer , product , and order
@app.route('/update_customer', methods=["POST"])
def update_customer():
    try:
        data = request.get_json()
        info = Customers.query.filter_by(customerId=data["customerId"]).first()
        print(info)
        if info is None:
            return jsonify({'status': 'no data found'})
        else:
            if data["customerId"]:
                info.customerId = data['customerId']
            if data["companyName"]:
                info.companyName = data['companyName']
            if data["contactName"]:
                info.contactName = data['contactName']
            if data["contactTitle"]:
                info.contactTitle = data['contactTitle']
            if data["address"]:
                info.address = data['address']
            if data["city"]:
                info.city = data['city']
            if data["region"]:
                info.region = data['region']
            if data["postalCode"]:
                info.postalCode = data['postalCode']
            if data["country"]:
                info.country = data['country']
            if data["phone"]:
                info.phone = data['phone']
            if data["fax"]:
                info.fax = data['fax']
            db.session.add(info)
            db.session.commit()
            return jsonify({'status': 'updated'})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/update_product', methods=["POST"])
def update_product():
    try:
        data = request.get_json()
        info = Products.query.filter_by(productId=data["productId"]).first()
        if info is None:
            return jsonify({'status': 'no data found'})
        else:
            if data["productId"]:
                info.productId = data['productId']
            if data["productName"]:
                info.productName = data['productName']
            if data["categoryId"]:
                info.categoryId = data['categoryId']
            if data["supplierId"]:
                info.supplierId = data['supplierId']
            if data["quantityPerUnit"]:
                info.quantityPerUnit = data['quantityPerUnit']
            if data["unitsInStock"]:
                info.unitsInStock = data['unitsInStock']
            if data["unitsOnOrder"]:
                info.unitsOnOrder = data['unitsOnOrder']
            if data["reorderLevel"]:
                info.reorderLevel = data['reorderLevel']
            if data["discontinued"]:
                info.discontinued = data['discontinued']
            db.session.add(info)
            db.session.commit()
            return jsonify({'status': 'updated'})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/update_order', methods=["POST"])
def update_order():
    try:
        data = request.get_json()
        info = Orders.query.filter_by(customerId=data["customerId"]).first()
        if info is None:
            return jsonify({'status': 'no data found'})
        else:
            if data["orderId"]:
                info.orderId =  data["orderId"],
            if data["customerId"]:
                info.customerId = data["customerId"],
            if data["employeeId"]:
                info.employeeId = data["employeeId"],
            if data["orderDate"]:
                info.orderDate = data["orderDate"],
            if data["requiredDate"]:
                info.requiredDate = data["requiredDate"],
            if data["shippedDate"]:
                info.shippedDate = data["shippedDate"],
            if data["shipVia"]:
                info.shipVia = data["shipVia"],
            if data["freight"]:
                info.freight=data["freight"],
            if data["shipName"]:
                info.shipName=data["shipName"],
            if data["shipAddress"]:
                info.shipAddress=data["shipAddress"],
            if data["shipCity"]:
                info.shipCity=data["shipCity"],
            if data["shipRegion"]:
                info.shipRegion = data["shipRegion"],
            if data["shipPostalCode"]:
                info.shipPostalCode=data["shipPostalCode"],
            if data["shipCountry"]:
                info.shipCountry=data["shipCountry"]
            db.session.add(info)
            db.session.commit()
            return jsonify({'status': 'updated'})
    except Exception as e:
        return jsonify({'error': str(e)})

#getting order history of a customer
@app.route('/order_history', methods=["POST"])
def order_history():
    try:
        print("in order_history")
        data = request.get_json()
        info = Orders.query.filter_by(customerId=data["customerId"]).all()
        result =[]
        for row in info:
            obj = {
                "orderId" :row.orderId,
                "customerId":row.customerId,
                "employeeId":row.employeeId,
                "orderDate" :row.orderDate,
                "requiredDate" :row.requiredDate,
                "shippedDate ":row.shippedDate,
                "shipVia":row.shipVia,
                "freight":row.freight,
                "shipName" :row.shipName,
                "shipAddress":row.shipAddress,
                "shipCity":row.shipCity,
                "shipRegion ":row.shipRegion,
                "shipPostalCode":row.shipPostalCode,
                "shipCountry":row.shipCountry
            }
            result.append(obj)
        return json.dumps(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
