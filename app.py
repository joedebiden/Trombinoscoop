from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Personne, Faculte, Campus
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from views import *
app = Flask(__name__)

app.config['SECRET_KEY'] = 'clé_secrete'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')

admin.add_view(ModelView(Personne, db.session))
admin.add_view(ModelView(Faculte, db.session))
admin.add_view(ModelView(Campus, db.session))


#permet de lancer le serveur juste en appelant le fichier python
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
