from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/welcome')
def welcome_world():
    return render_template('welcome.html', user = request.args.get('username'))