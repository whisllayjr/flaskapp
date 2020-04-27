from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"