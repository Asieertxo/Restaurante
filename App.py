from flask import Flask, render_template, request, redirect, url_for,flash
from ensurepip import bootstrap
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# MySQL conn
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'restaurante'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

#importacion de la capeta de imagenes
picFolder = os.path.join('static', 'img')
app.config['UPLOAD_IMG'] = picFolder

#importacion de la capeta de imagenes
styleFolder = os.path.join('static', 'css')
app.config['UPLOAD_STYLE'] = styleFolder
css = os.path.join(app.config['UPLOAD_STYLE'], 'style.css')
bootstraps = os.path.join(app.config['UPLOAD_STYLE'], 'bootstrap.min.css')
styles = [css, bootstraps]



@app.route('/')
def Index():
    conn = mysql.connection.cursor()
    conn.execute('SELECT * FROM menu')
    menu = conn.fetchall()
    
    img = os.path.join(app.config['UPLOAD_IMG'], 'prueba.jpg')

    return render_template('index.html', menu = menu, img = img, styles = styles)



@app.route('/add_client', methods=['POST'])
def add_client():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']

        conn = mysql.connection.cursor()
        conn.execute('INSERT INTO clientes(nombre, email, pass) VALUES (%s, %s, %s)',
        (nombre, email, password))
        flash('Contacto agregado')
        mysql.connection.commit()

        return redirect(url_for('Index'))









@app.route('/menu')
def menu():
    return 'Menu'



if __name__ == '__main__':
    app.run(port = 3000, debug = True)