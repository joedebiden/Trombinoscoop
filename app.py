from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 

@app.route("/")
def root():
    return render_template("welcome.html")

@app.route("/success")
def success():
    return "Connecté avec succès!"


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'email' not in request.form or 'password' not in request.form:
            error = "Veuillez entrer une addresse mail et un mot de passe"
            return render_template('login.html', error=error)
        else:
            email = request.form['email']
            password = request.form['password']

            if email != 'test@mail' or password != 'test@mail':
                error = "Adresse mail ou mot de passe erroné."
                return render_template('login.html', error=error)
            else:
                return redirect(url_for("root"))
    else:
        return render_template('login.html')




#permet de lancer le serveur juste en appelant le fichier python 
if __name__ == '__main__':
    app.run(debug=True)
