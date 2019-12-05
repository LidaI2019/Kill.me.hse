from flask import Flask

from models import db, Men
from routse import api, index

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.add(Men(name='Bob', surname='I', age=29))
    db.session.add(Men(name='Rocky', surname='Y', age=19))
    db.session.commit()


if __name__ == '__main__':
    app.run()


