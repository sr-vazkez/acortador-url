#Importando librerias
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_mysql_connector import MySQL
import shourtuuid

#Inicializando app
app = Flask(__name__)

#endpoint