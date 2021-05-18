#Importando librerias
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_mysql_connector import MySQL
import shourtuuid

#Inicializando app
app = Flask(__name__)

#endpoint
endpoint = 'http://short.url'

#conexion a Mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE'] = 'db_enlaces_cortos'

#Inicializando BD
mysql = MySQL(app)

#rutas
@app.route('/', methods = ['GET'])
def inicio():
     try:
          return jsonify(respuesta = 'inicio')
     except:
          return jsonify(respuesta = 'Error de peticion'), 500
     


#Ejecutar app
if __name__ == "__main__":
     app.run(port=80, debug=True)
    