from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Table de jointure pour la relation "amis"
amis_association = db.Table(
    'amis',
    db.Column('personne_id', db.Integer, db.ForeignKey('personne.id'), primary_key=True),
    db.Column('ami_id', db.Integer, db.ForeignKey('personne.id'), primary_key=True)
)


class Faculte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    couleur = db.Column(db.String(6))

    def __repr__(self):
        return f"<Faculte {self.nom}>"


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

    faculte_id = db.Column(db.Integer, db.ForeignKey('faculte.id'))
    campus_id = db.Column(db.Integer, db.ForeignKey('campus.id'))
    # CURSUS a faire

    # Relation many-to-many avec la même table Personne (amis)
    amis = db.relationship('Personne',
                           secondary=amis_association,
                           primaryjoin=(amis_association.c.personne_id == id),
                           secondaryjoin=(amis_association.c.ami_id == id),
                           backref='amis_inverse')

    def __repr__(self):
        return f'<Personne {self.nom} {self.prenom}>'


class Employe(Personne):
    bureau = db.Column(db.String(30))
    campus = db.ForeignKey('Campus')
    fonction = db.ForeignKey('Fonction')

    def __repr__(self):
        return f'<Employe {self.nom} {self.prenom}>'


class Etudiant(Personne):
    cursus_id = db.Column(db.Integer, db.ForeignKey('cursus.id'))
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
