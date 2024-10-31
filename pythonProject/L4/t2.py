from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/names')
def name_fun():
    return "Hi"


if __name__ == '__main__':
    app.run()
