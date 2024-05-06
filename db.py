from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/realestateapp'
app.config['SQLALCHEMY_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Users(db.Model):
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(80), unique=False, nullable=False)
    userAddress = db.Column(db.String(120), unique=True, nullable=False)
    userPhoneNo = db.Column(db.String(80), unique=True, nullable=False)
    userEmail = db.Column(db.String(80), unique=True, nullable=False)


class Details(db.Model):
        dId = db.Column(db.Integer, primary_key=True, autoincrement=True)
        bedroom = db.Column(db.Integer, unique=False, nullable=True)
        washroom = db.Column(db.Integer, unique=False, nullable=True)
        floors = db.Column(db.Integer, unique=False, nullable=False)
        lawn = db.Column(db.String(80), unique=False, nullable=False)


class Properties(db.Model):
    propertyId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.String(80), unique=False, nullable=False)
    Ptype = db.Column(db.String(80), unique=False, nullable=False)
    Plocation = db.Column(db.String(80), unique=False, nullable=False)
    purpose = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.String(80), unique=False, nullable=False)
    dId = db.Column(db.Integer, unique=True, nullable=False)
    userId = db.Column(db.Integer, unique=True, nullable=False)


if __name__ == '__main__':
        app.run(debug=True)