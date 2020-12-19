from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/contact')
def contact():
    return 'I dont want to share my contact :)'

if __name__ == "__main__":
    app.run(debug=True)