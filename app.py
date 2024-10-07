from flask import Flask, render_template

app = Flask(__name__) 

@app.route("/")
def root():
    return render_template("welcome.html")

@app.route("/login")
def login():
    return render_template("login.html")


#permet de lancer le serveur juste en appelant le fichier python 
if __name__ == '__main__':
    app.run()
