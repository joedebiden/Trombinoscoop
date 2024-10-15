from flask import Flask
from flask_session import Session
from models import db
from admin import init_admin

app = Flask(__name__)
app.secret_key = 'ma_clé_secrète'

app.config['SECRET_KEY'] = 'clé_secrete'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True     #signe les cookies

Session(app)
db.init_app(app)
init_admin(app)


from views import *


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)