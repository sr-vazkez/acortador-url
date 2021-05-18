#Importando librerias
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_mysql_connector import MySQL
import shourtuuid

#Inicializando app
app = Flask(__name__)

#endpoint
endpoint = 'http://short.url'

#Ejecutar app
if __name__ == "__main__":
     app.run(port=80, debug=True)
    