from flask import Blueprint, jsonify

from models import db, Car, Doorcount

index = Blueprint('index', __name__, url_prefix='/')
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/cars')
def get_cars():
    return jsonify([(lambda car: car.json()) (car) for car in Car.query.all()])

@api.route('/car/id/<int:car_id>')
def get_car(car_id):
    car = Car.query.get (car_id)
    return jsonify(car.json()) if car else ''

@api.route('/car/add/horsepower=<string:car_horsepower>;torque=<string:car_torque>;cargo_volume=<string:car_cargo_volume>;doorcount_id=<int:doorcount_id>')
def put_car(car_horsepower, car_torque, car_cargo_volume, doorcount_id):
    car = Car(horsepower=car_horsepower, torque=car_torque, cargo_volume=car_cargo_volume, doorcount_id=doorcount_id)
    db.session.add(car)
    db.session.commit()
    return jsonify(car.json())

@index.route('/')
@index.route('/index')
def get_index():
    return'''
    <html>
       <title>
           Mega RESTful web service
       </title>
       <body>
           <h3>API:</h3>
           <a href="./api/cars">Cars</a>
       </body>
    </html>
          '''

@api.route('/doorcounts')
def get_doorcounts():
    return jsonify([(lambda doorcount: doorcount.json()) (doorcount) for doorcount in Doorcount.query.all()])

@api.route('/doorcount/id/<int:doorcount_id>')
def get_doorcount(doorcount_id):
    doorcount = Doorcount.query.get (doorcount_id)
    return jsonify(doorcount.json()) if doorcount else ''

@api.route('/doorcount/add/name=<string:doorcount_name>')
def put_doorcount(doorcount_name):
    doorcount = Doorcount(name=doorcount_name)
    db.session.add(doorcount)
    db.session.commit()
    return jsonify(doorcount.json())

