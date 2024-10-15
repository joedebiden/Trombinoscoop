from flask import render_template, request, redirect, url_for, flash, session
from app import app
from forms import LoginForm, StudentProfileForm
from models import Personne, db


@app.route("/", methods=["GET", "POST"])
@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    if 'logged_user_id' in session:
        logged_user_id = session['logged_user_id']
        logged_user = Personne.query.filter_by(id=logged_user_id).first()
        return render_template('welcome.html', logged_user=logged_user)
    else:
        return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # Utilisation de validate_on_submit()
        user_email = form.email.data   # Corrigé l'accès à l'email
        logged_user = Personne.query.filter_by(email=user_email).first()
        if logged_user:
            session['logged_user_id'] = logged_user.id
            return redirect(url_for('welcome'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = StudentProfileForm()

    if form.validate_on_submit():  # Vérifie si le formulaire est valide
        nouvelle_personne = Personne(
            nom=form.nom.data,
            prenom=form.prenom.data,
            matricule=form.matricule.data,
            email=form.email.data,
            tel_fix=form.tel_fix.data,
            tel_mobile=form.tel_mobile.data,
            password=form.password.data,  # Hacher le mot de passe avant de l'enregistrer
            date_naissance=form.date_naissance.data,
            faculte_id=form.faculte.data.id,
            campus_id=form.campus.data.id
        )

        # Ajouter l'utilisateur à la base de données
        db.session.add(nouvelle_personne)
        db.session.commit()  # Sauvegarder les modifications

        flash('Compte créé avec succès')
        return redirect(url_for('login'))  # Rediriger après la soumission réussie

    return render_template('register.html', form=form)  # Rendre la page avec le formulaire
