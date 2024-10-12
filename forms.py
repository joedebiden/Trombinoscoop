from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField
from wtforms.fields.simple import TelField
from wtforms.validators import DataRequired, Email
from models import db, Personne, Etudiant


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
    # Champs de base
    first_name = StringField('Prénom', validators=[DataRequired()])
    last_name = StringField('Nom', validators=[DataRequired()])
    birth_date = DateField('Date de naissance', format='%Y-%m-%d', validators=[DataRequired()])
    matricule = StringField('Matricule', validators=[DataRequired()])

    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = TelField('Téléphone fixe', validators=[DataRequired()])
    mobile_phone = TelField('Téléphone mobile', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])

    # Champs supplémentaires
    faculte = StringField('Faculté', validators=[DataRequired()])
    cursus = StringField('Cursus', validators=[DataRequired()])
    annee = StringField('Année', validators=[DataRequired()])

    # liste de séleciton
    campus = SelectField('Campus', choices=[('Campus1', 'Campus 1'), ('Campus2', 'Campus 2')],
                         validators=[DataRequired()])
    fonction = SelectField('Fonction', choices=[('Etudiant', 'Étudiant'), ('Professeur', 'Professeur')],
                           validators=[DataRequired()])

    # Méthode save
    def save(self, commit=True):
        pass