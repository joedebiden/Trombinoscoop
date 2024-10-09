from flask_admin import Admin
from models import db, Personne, Faculte, Campus, Fonction, Cursus, Employe, Etudiant, Message
from flask_admin.contrib.sqla import ModelView

def init_admin(app):
    # Initialiser Flask-Admin après que l'app soit passée en paramètre
    admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')

    admin.add_view(ModelView(Personne, db.session))
    admin.add_view(ModelView(Faculte, db.session))
    admin.add_view(ModelView(Campus, db.session))
    admin.add_view(ModelView(Fonction, db.session))
    admin.add_view(ModelView(Cursus, db.session))
    admin.add_view(ModelView(Employe, db.session))
    admin.add_view(ModelView(Etudiant, db.session))
    admin.add_view(ModelView(Message, db.session))
