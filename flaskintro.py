from flask import Flask, request
import requests
import psycopg2

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/test')
def hello_test():
    return 'Hello, test'


@app.route('/login', methods=['GET', 'POST'])
def one_requests():
    if request.method == 'GET':
        return '<h1>GET REQUEST</h1>'
    elif request.method == 'POST':
        request.form('incoming')
        print(data)
        return 'Made a POST request'


@app.route('/put', methods=['PUT', 'DELETE'])
def two_requests():
    if request.method == 'PUT':
        return 'Made a PUT request'
    elif request.method == 'DELETE':
        return 'Made a DELETE request'
