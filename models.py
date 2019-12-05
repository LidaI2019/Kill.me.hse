from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))
    age = db.Column(db.Integer)
    position_id = db.Column(db.Integer, ForeignKey('Position.id'))
    position = relationship('Position')

    def json(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "age": self.age, "position": self.position.json()}

class Position(db.Model):
    __tablename__ = 'Position'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    def json(self):
        return {"id":self.id, "name": self.name}
