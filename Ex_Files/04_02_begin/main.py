from distutils.log import debug
from flask import Flask

app = Flask(__name__)

Fruits = ["Apple", "Orange", "Kiwi", "Banana"]

@app.route("/")
def hello():
  return f'My favorite fruit is an {Fruits[1]}'

app.run(debug=True)