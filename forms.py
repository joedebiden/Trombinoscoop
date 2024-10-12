from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length
from models import db, Personne, Faculte, Campus, Cursus
from wtforms_alchemy import QuerySelectField

class LoginForm(FlaskForm):
    email = StringField('Mail : ', validators=[DataRequired(), Email()])
    password = PasswordField('Password : ', validators=[DataRequired()])

    def validate_login(self):
        if not FlaskForm.validate(self):
            return False

        email = self.email.data
        password = self.password.data
        result = Personne.query.filter_by(email=email, password=password).all()

        if len(result) != 1:
            self.email.errors.append("Adresse mail ou mot de passe erroné(e).")
            return False

        return True


class StudentProfileForm(FlaskForm):
    # attributs de la classe Personne
    nom = StringField('Nom : ', validators=[DataRequired(), Length(max=30)])
    prenom = StringField('Prenom : ', validators=[DataRequired(), Length(max=30)])
    date_naissance = DateField('Date de naissance : ', validators=[DataRequired()])
    matricule = StringField('Matricule : ', validators=[DataRequired(), Length(max=10)])
    email = StringField('Mail : ', validators=[DataRequired(), Length(max=120)])
    tel_fix = StringField('Telephone fixe: ')
    tel_mobile = StringField('Telephone mobile: ')
    password = PasswordField('Mot de passe : ', validators=[DataRequired(), Length(min=4, max=60)])

    #cursus = QuerySelectField('Cursus', query_factory=lambda: Cursus.query.all(), #a ajouter aussi meme condition que dans la route register
                                #get_label='nom', allow_blank=False)
    faculte = QuerySelectField('Faculté', query_factory=lambda: Faculte.query.all(),
                               get_label='nom', allow_blank=False)
    campus = QuerySelectField('Campus', query_factory=lambda: Campus.query.all(),
                              get_label='nom', allow_blank=False)
    submit = SubmitField('Créer un compte')
