from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'



@app.route('/test')
def hello_test():
    return 'Hello, test'

@app.route('/get', methods=['GET', 'POST'])
def requests():
    if request.method == 'GET':
        return 'Made a GET request'
    elif request.method == 'POST':
        return 'Made a POST request'
