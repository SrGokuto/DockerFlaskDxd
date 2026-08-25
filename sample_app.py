import os
import pymysql
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=os.environ.get('MYSQL_HOST', 'servidor-bd'),
            user=os.environ.get('MYSQL_USER', 'root'),
            password=os.environ.get('MYSQL_ROOT_PASSWORD', 'sena123'),
            database=os.environ.get('MYSQL_DATABASE', '082_db')
        )
        conn.close()
        db_status = "Conexion exitosa a la base de datos"
    except Exception as e:
        db_status = f"Error al conectar a la base de datos: {e}"

    return f"<h1>Bienvenido a mi aplicacion Flask</h1><p>{db_status}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=False)
