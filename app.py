from flask import Flask

app = Flask(__name__)

#create routes
@app.route('/')
def hello_world():
    return 'Hello world'

