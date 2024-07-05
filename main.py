from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/secret')
def secret_page():
    return "This is secret page"

if __name__ == '__main__':
    app.run(debug=True)