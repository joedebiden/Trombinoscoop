from flask import Flask, render_template, request, redirect, url_for, flash

@app.route("/")
@app.route("/welcome")
def root():
    return render_template("welcome.html")


@app.route("/success")
def success():
    return redirect(url_for("root"))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'email' not in request.form or 'password' not in request.form:
            error = "Veuillez entrer une addresse mail et un mot de passe"
            return render_template('login.html', error=error)
        else:
            email = request.form['email']
            password = request.form['password']
            if email != 'test@mail':
                error = "Adresse mail erroné."
                return render_template('login.html', error=error)
            elif password != 'test@mail':
                error = "Mot de passe erroné."
                return render_template('login.html', error=error)
            else:
                return redirect(url_for("success"))
    else:
        return render_template('login.html')
