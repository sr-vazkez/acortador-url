# Importando librerias
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_mysql_connector import MySQL
import shortuuid

# Inicializando app
app = Flask(__name__)

# endpoint
endpoint = 'http://127.0.0.1:5500'

# conexion a Mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DATABASE'] = 'db_enlaces_cortos'

# Inicializando BD
mysql = MySQL(app)

# rutas

# Ruta inicial


@app.route('/', methods=['GET'])
def inicio():
    try:
        return jsonify(respuesta='inicio')
    except:
        return jsonify(respuesta='Error de peticion'), 500

# Ruta para crear enlace corto


@app.route('/crear_enlace_corto', methods=['POST'])
def crear_enlace_corto():
    try:
        if request.method == 'POST':
            # capturando la url
            url = request.form['url']

            # cursor
            cursor = mysql.connection.cursor()

            # Ciclo para valdar enlace corto y no se duplique
            while True:
                # generando enlace corto
                enlace_corto = shortuuid.ShortUUID().random(length=7)
                # Consultamos a la base de datos si existe el enlace
                cursor.execute(
                    "SELECT * FROM ENLACES WHERE ENLACE_CORTO = BINARY %s", (enlace_corto))

                if not cursor.fetchone():
                    break
            # Consultamos si en la base de datos existe la URL
            cursor.execute(
                "SELECT enlace_coro FROM enlaces WHERE URL = BINARY %s", (url,))
            data = cursor.fetchone()
            if data:
                nuevo_enlace = endpoint + '/'+data[0]
                return jsonify(respuesta=nuevo_enlace)

            # Ingresamos en la base de datos  la url enviada
            cursor.execute(
                "INSERT INTO enlaces (url, enlace_corto)VALUES (%s, %s)", (url, enlace_corto))

            # Guardae cambios en la base de datos
            mysql.connection.commit()

            # Cerrar conexion
            cursor.close()
            nuevo_enlace = endpoint + '/' + enlace_corto
            return jsonify(respuesta=nuevo_enlace)
    except:
        return jsonify(respuesta='Error de peticion'), 500

# Ruta para ir a URL de base de datos


@app.route('/<id>')
def obtener_url(id):
    try:
        cursor = mysql.connection.cursor()

        # buscamos en la bd la direccion url
        cursor.execute(
            "SELECT url FROM enlaces WHERE enlace_corto = BINARY %s", (id,))

        # Guardar en variable el resultado
        data = cursor.fetchone()

        # cerrar conexion de la base de datos
        cursor.close()
        return jsonify(respuesta=data[0]), 200
    except:
        pass


# Ejecutar app
if __name__ == "__main__":
    app.run(port=5500, debug=True)
