from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email
from models import Personne

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