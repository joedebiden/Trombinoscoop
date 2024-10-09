from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Personne, Faculte, Campus, Fonction, Cursus, Employe, Etudiant, Message
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['SECRET_KEY'] = 'clé_secrete'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')

admin.add_view(ModelView(Personne, db.session))
admin.add_view(ModelView(Faculte, db.session))
admin.add_view(ModelView(Campus, db.session))
admin.add_view(ModelView(Fonction, db.session))
admin.add_view(ModelView(Cursus, db.session))
admin.add_view(ModelView(Employe, db.session))
admin.add_view(ModelView(Etudiant, db.session))
admin.add_view(ModelView(Message, db.session))

from views import *



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        root()
    app.run(debug=True)
