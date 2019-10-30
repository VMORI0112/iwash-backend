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
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname
        }