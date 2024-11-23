from flask import Flask, render_template, jsonify

app = Flask(__name__)
names_data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

@app.route('/')
def home():
    return "<h1>Hello World!</h1>"


@app.route('/names')
def name_fun():
    return jsonify(names_data)


if __name__ == '__main__':
    app.run()
