from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
    redirect(url_for('greetings'))
@app.route('/greetings')
def greetings():
    return 'How are you?'