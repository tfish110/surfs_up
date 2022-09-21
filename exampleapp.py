from flask import Flask

exampleapp = Flask(__name__)

@exampleapp.route('/')
def hello_world():
    return 'Hello world'