from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'I am a secret. Shhhhhh!'

@app.route("/")
def land():
    return render_template('home.html')