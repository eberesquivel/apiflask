
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


""" Inicia la aplicacion """
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

""" Base de Datos """
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

""" Inicia la DB """

db = SQLAlchemy(app)

""" Inicia Marshmallow """

ma = Marshmallow(app)

""" CLase Producto Modelo """

class Producto(db.Model):
    id = db.Column(db.Integer, primaryKey=True)
    nombre = db.Column(db.String(100),unique=True)
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float)
    cantidad = db.Column(db.Integer)

    def __init__(self,nombre,descripcion,precio,cantida):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

""" Schema Producto """

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ['id','nombre', 'descripcion', 'precio','cantidad']


""" Inicia el Schema """

producto_schema = ProductoSchema(strict=True)
producto_schema= ProductoSchema(many=True,strict=True)


@app.route('/')
def get():
    return  jsonify({'msg':'Hola Mundo'})


""" Corre el servidor """

if  __name__ == '__main__':
    app.run(debug=True)