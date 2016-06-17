from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('index.html', hd_health="hello MoTo")


if "__main__" == __name__:
    app.run(host='127.0.0.1', port=5000)
