from flask import Flask

from models import db, Car, Doorcount
from routse import api, index

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    doors_5 = Doorcount(name='5doors')
    doors_4 = Doorcount(name='4doors')
    db.session.add(doors_5)
    db.session.add(doors_4)
    db.session.commit()
    db.session.add(Car(horsepower='248', torque='273', cargo_volume=24, doorcount_id=doors_5.id))
    db.session.add(Car(horsepower='247', torque='256', cargo_volume=25, doorcount_id=doors_4.id))
    db.session.commit()


if __name__ == '__main__':
    app.run()


