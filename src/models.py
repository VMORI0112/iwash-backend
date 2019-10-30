from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120) )
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname
        }

class Washers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(220))
    number = db.Column(db.Integer())
    cicle_1 = db.Column(db.String(120))
    time_1 = db.Column(db.Integer())
    price_1 = db.Column(db.Float(5))
    cicle_2 = db.Column(db.String(120))
    time_2 = db.Column(db.Integer())
    price_2 = db.Column(db.Float(5))
    cicle_3 = db.Column(db.String(120))
    time_3 = db.Column(db.Integer())
    price_3 = db.Column(db.Float(5))
    cicle_4 = db.Column(db.String(120))
    time_4 = db.Column(db.Integer())
    price_4 = db.Column(db.Float(5))
    cicle_5 = db.Column(db.String(120))
    time_5 = db.Column(db.Integer())
    price_5 = db.Column(db.Float(5))

    def __repr__(self):
        return '<Washers %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "number": self.number,
            "cicle1": self.cicle1,
            "time1": self.time1,
            "price1": self.price1,
            "cicle2": self.cicle2,
            "time2": self.time2,
            "price2": self.price2,
            "cicle3": self.cicle3,
            "time3": self.time3,
            "price3": self.price3,
            "cicle4": self.cicle4,
            "time4": self.time4,
            "price4": self.price4,
            "cicle5": self.cicle5,
            "time5": self.time5,
            "price5": self.price5
        }

class Dryers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(220))
    number = db.Column(db.Integer())
    cicle = db.Column(db.String(120))
    time = db.Column(db.Integer())
    price = db.Column(db.Float(5))

    def __repr__(self):
        return '<Dryers %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "number": self.number,
            "cicle": self.cicle,
            "time": self.time,
            "price": self.price
        }