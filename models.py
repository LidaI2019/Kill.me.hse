from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    horsepower = db.Column(db.Integer)
    torque = db.Column(db.Integer)
    cargo_volume = db.Column(db.Integer)
    doorcount_id = db.Column(db.Integer, ForeignKey('Doorcount.id'))
    doorcount = relationship ('Doorcount')

    def json(self):
        return {"id": self.id, "horsepower": self.horsepower, "torque": self.torque, "cargo_volume": self.cargo_volume, "doorcount": self.doorcount.json()}

class Doorcount(db.Model):
    __tablename__ = 'Doorcount'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    def json(self):
        return {"id":self.id,"name":self.name}
