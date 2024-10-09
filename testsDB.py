from datetime import datetime
from app import app, db
from models import Personne

#create DB
with app.app_context():
    db.create_all()


# Ajout d'un enregistrement
def add_personne():
    with app.app_context():
        nouvelle_personne = Personne(
            matricule='0123456789',
            nom='dupont',
            prenom='xavier',
            date_naissance='1990-01-01',
            emai='jean.dupont@mail.com',
            password='password'
        )
        db.session.add(nouvelle_personne)
        db.session.commit()


#recup des enregistrements
def get_personne():
    with app.app_context():
        personnes = Personne.query.all()
        for personne in personnes:
            print(personne.nom, personne.prenom)


#modif d'un enregistrement
def update_personne():
    with app.app_context():
        personne = Personne.query.get(id) #id de la personne
        if personne:
            personne.nom = "Durand"
            db.session.commit()

