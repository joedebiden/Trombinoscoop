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
@app.route("/register" , methods=['GET', 'POST'])
def register():
    form = StudentProfileForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save(commit=True)
        return redirect(url_for('success'))
    else:
        return render_template('user_profile.html', form=form)



