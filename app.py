from flask import Flask

from models import db, Employee, Position
from routse import api, index

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    manager = Position(name='Manager')
    developer = Position(name='Developer')
    db.session.add(manager)
    db.session.add(developer)
    db.session.commit()
    db.session.add(Employee(name='Bob', surname='I', age=29, position_id=manager.id))
    db.session.add(Employee(name='Rocky', surname='Y', age=19, position_id=developer.id))
    db.session.commit()


if __name__ == '__main__':
    app.run()


