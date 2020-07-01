
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask_sqlalquemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


""" Inicia la aplicacion """
app = Flask(__name__)

@app.route('/')
def get():
    return  jsonify({'msg':'Hola Mundito'})


""" Corre el servidor """

if  __name__ == '__main__':
    app.run(debug=True)