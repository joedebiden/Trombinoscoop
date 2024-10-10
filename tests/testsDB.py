from datetime import datetime
from app import app, db
from models import *


# Créer la base de données
with app.app_context():
    db.create_all()

    

# Ajout d'un enregistrement
def AddPersonne():
    with app.app_context():
        AddPersonne = Personne(
            matricule='0123456789',
            nom='Dupont',
            prenom='Xavier',
            date_naissance=datetime.strptime('1990-01-01', '%Y-%m-%d').date(),
            email='jean.dupont@mail.com',
            password='password'  # Gère ce champ avec du hashing dans un projet réel
        )
        db.session.add(AddPersonne)
        db.session.commit()
        print("Personne ajoutée :", AddPersonne.nom, AddPersonne.prenom)

# Récupération des enregistrements
def GetPersonne():
    with app.app_context():
        personnes = Personne.query.all()
        for personne in personnes:  
            print(f"Nom: {personne.nom}, Prénom: {personne.prenom}, Matricule: {personne.matricule}")

# Modification d'un enregistrement
def UpdatePersonne(personne_id):
    with app.app_context():
        personne = Personne.query.get(personne_id)  # id de la personne
        if personne:
            personne.nom = "Durand"
            db.session.commit()
            print(f"Personne mise à jour : {personne.nom}")
        else:
            print(f"Personne avec l'ID {personne_id} non trouvée.")


AddPersonne()
GetPersonne()
UpdatePersonne(1)

