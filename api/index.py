from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! trying something for just a change'

@app.route('/about')
def about():
    return 'About'

