from flask import Flask

# All Flask applications require this first
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/<name>')
def print_name(name): # we need to pass the param from the Flask.route to the python native function hence we see 'name' on the function and in the route
    return 'Hi, {}'.format(name)

