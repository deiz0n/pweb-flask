from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/sobre")
def about():
    return render_template('about.html')

@app.route("/experiencia")
def experience():
    return render_template('experience.html')

@app.route("/formacao")
def training():
    return render_template('training.html')

@app.route("/contato")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
