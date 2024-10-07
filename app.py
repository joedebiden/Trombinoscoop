from flask import Flask, render_template

app = Flask(__name__) 

@app.route("/")
def root():
    return render_template("welcome.html")

@app.route("/login")
def login():
    return render_template("login.html")

def login(request):
    if len(request.POST) > 0:
        if 'email'not in request.POST or 'password' not in request.POST:
            error = "Veuillez entrer une adresse de courriel et un mot de passe."
            return render_template("login.html", {'error' : error})
        else:
            email = request.POST['email']
            password = request.POST['password']

            if password != 'sesame' or email != 'test@mail':
                error = "Adresse mail ou mot de passe erroné."
                return render_template('login.html', {'error' : error})
            else:
                return Flask.route('/welcome')
    else:
        return render_template('login.html')


#permet de lancer le serveur juste en appelant le fichier python 
if __name__ == '__main__':
    app.run()
