from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date, String, Integer


db = SQLAlchemy()



class Personne(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    matricule = db.Column(db.String(10), nullable=False)
    nom = db.Column(db.String(30), nullable=False)
    prenom = db.Column(db.String(30), nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel_fix = db.Column(db.String(20))
    tel_mobile = db.Column(db.String(20))
    password = db.Column(db.String(60), nullable=False)  #ne pas stocker le mot de passe ene clair
    amis = db.relationship("Self")
    faculte = db.ForeignKey('Faculte')

    def __repr__(self):
        return f'<Personne {self.nom} {self.prenom}>'
    


class Employe(Personne):
    bureau = db.Column(db.String(30))
    campus = db.ForeignKey('Campus')
    fonction = db.ForeignKey('Fonction')

    def __repr__(self):
        return f'<Employe {self.nom} {self.prenom}>'
    

    
class Etudiant(Personne):
    cursus = db.ForeignKey('Cursus')
    annee = db.Column(db.Integer)

    def __repr__(self):
        return f'<Etudiant {self.nom} {self.prenom}>'
    



class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auteur_id = db.Column(db.Integer, db.ForeignKey('personne.id'), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_publication = db.Column(db.DateTime, nullable=False)

    # Relation avec la table Personne
    auteur = db.relationship('Personne', backref='messages')

    def __repr__(self):
        return f"<Message {self.contenu[:20]}...>"



class Faculte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    couleur = db.Column(db.String(6))

    def __repr__(self):
        return f"<Faculte {self.nom}>"
    


class Campus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    addresse_postale = db.Column(db.String(60))

    def __repr__(self):
        return f"<Campus {self.nom}>"



class Fonction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"<Fonction {self.intitule}>"



class Cursus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"<Cursus {self.intitule}>"






#    def __repr__(self):
#        return f'<Personne {self.nom} {self.prenom}>'
