from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

@app.route('/vivek')
def hello_vivek():
    return "Hello Vivek"

if __name__ == '__main__':
    app.run(debug=True)