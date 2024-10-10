from flask import render_template, request, redirect, url_for, flash
from app import app
from forms import LoginForm, StudentProfileForm
from models import Personne, db


@app.route("/")
@app.route("/welcome")
def root():
    return render_template("welcome.html")


@app.route("/success")
def success():
    return redirect(url_for("root"))


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted() and form.validate_login():
        return redirect(url_for('success'))
    return render_template('login.html', form=form)


# route à surveiller et à tester
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = StudentProfileForm()

    if form.validate_on_submit():  # Vérifie si le formulaire a été soumis et est valide
        # Sauvegarde les données après validation
        new_user = Personne(
            email=form.email.data,
            password=form.password.data,
            # Ajoute d'autres champs ici
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Inscription réussie. Veuillez vous connecter.", "success")
        return redirect(url_for('login'))  # Redirige vers la page de connexion après inscription réussie
    else:
        # En cas d'erreur, affiche la page d'inscription avec le formulaire et les erreurs
        return render_template('register.html', form=form)




