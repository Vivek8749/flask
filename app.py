from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
    return f"Hello {name} how are you?"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)