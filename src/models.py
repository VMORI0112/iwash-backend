from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120) )
    password = db.Column(db.String(80), nullable=False)
    avatar = db.Column(db.String(220), default='../../../img/avatar/avatar.png')
    wallet = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Users %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "avatar": self.avatar,
            "wallet": self.wallet
        }

class Washers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(220))
    number = db.Column(db.Integer())
    postal = db.Column(db.Integer())
    locationNum = db.Column(db.Integer())
    available = db.Column(db.String(12), default='available')
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
            "postal": self.postal,
            "locationNum": self.locationNum,
            "available": self.available,
            "cicle_1": self.cicle_1,
            "time_1": self.time_1,
            "price_1": self.price_1,
            "cicle_2": self.cicle_2,
            "time_2": self.time_2,
            "price_2": self.price_2,
            "cicle_3": self.cicle_3,
            "time_3": self.time_3,
            "price_3": self.price_3,
            "cicle_4": self.cicle_4,
            "time_4": self.time_4,
            "price_4": self.price_4,
            "cicle_5": self.cicle_5,
            "time_5": self.time_5,
            "price_5": self.price_5
        }

class Dryers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(220))
    number = db.Column(db.Integer())
    postal = db.Column(db.Integer())
    locationNum = db.Column(db.Integer())
    available = db.Column(db.String(12), default='available')
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
            "postal": self.postal,
            "locationNum": self.locationNum,
            "available": self.available,
            "cicle": self.cicle,
            "time": self.time,
            "price": self.price
        }