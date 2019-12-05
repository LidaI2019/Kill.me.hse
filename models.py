from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Men(db.Model):
    __tablename__ = 'mens'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))
    age = db.Column(db.Integer)

    def json(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "age": self.age}

