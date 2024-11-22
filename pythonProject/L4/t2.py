from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/names')
def name_fun():
    return "Avi, Benny, Moshe x2"


if __name__ == '__main__':
    app.run()
