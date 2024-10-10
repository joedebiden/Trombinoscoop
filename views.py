from flask import render_template, request, redirect, url_for, flash
from app import app
from forms import LoginForm

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
