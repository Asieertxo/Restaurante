from ast import dump
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

from datetime import date
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

#importacion de estilos
styleFolder = os.path.join('static', 'css')
app.config['UPLOAD_STYLE'] = styleFolder
bootstraps = os.path.join(app.config['UPLOAD_STYLE'], 'bootstrap.min.css')
css_body = os.path.join(app.config['UPLOAD_STYLE'], 'style-body.css')
css_header = os.path.join(app.config['UPLOAD_STYLE'], 'style-header.css')
css_footer = os.path.join(app.config['UPLOAD_STYLE'], 'style-footer.css')
css_index = os.path.join(app.config['UPLOAD_STYLE'], 'style-index.css')
css_carta = os.path.join(app.config['UPLOAD_STYLE'], 'style-carta.css')
css_locales = os.path.join(app.config['UPLOAD_STYLE'], 'style-locales.css')
css_faqs = os.path.join(app.config['UPLOAD_STYLE'], 'style-faqs.css')

styles = {"bootstrap": bootstraps, "body": css_body, "header": css_header, "footer": css_footer, "index": css_index, "carta": css_carta, "locales": css_locales, "faqs": css_faqs}


##############################################################################################################HOME
@app.route('/')
def index():
    return render_template('index.html', styles = styles)







##############################################################################################################CARTA
@app.route('/carta')
def carta():
    conn = mysql.connection.cursor()
    conn.execute('SELECT * FROM carta')
    carta = conn.fetchall()

    #img = os.path.join(app.config['UPLOAD_IMG'], 'prueba.jpg')

    return render_template('carta.html', carta = carta, styles = styles)







##############################################################################################################LOCALES
@app.route('/locales')
def locales():
    return render_template('locales.html', styles = styles)













##############################################################################################################FAQS
@app.route('/faqs')
def faqs():



    conn = mysql.connection.cursor()
    conn.execute('SELECT * FROM faqs')
    faqs = conn.fetchall()
    return render_template('faqs.html',faqs = faqs, styles = styles)


@app.route('/añadir_comentario', methods=['POST'])
def añadir_comentario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        mensaje = request.form['mensaje']
        likes = 0
        fecha = date.today()
        print(fecha)

        conn = mysql.connection.cursor()
        conn.execute('INSERT INTO faqs(nombre, apellido, email, mensaje, likes, fecha) VALUES (%s, %s, %s, %s, %s, %s)',
        (nombre, apellido, email, mensaje, likes, fecha))
        flash('Pregunta guardada')
        mysql.connection.commit()

        return redirect(url_for('faqs'))


@app.route('/sumar_like', methods=['POST'])
def sumar_like():
    if request.method == 'POST':
        id = request.form['id']
        likes = int(request.form['likes']) + 1

        conn = mysql.connection.cursor()
        conn.execute('UPDATE faqs SET likes = %s WHERE id = %s',
        (likes, id))
        mysql.connection.commit()

        return redirect(url_for('faqs'))








##############################################################################################################PEDIDOS
@app.route('/pedido')
def pedido():
    return "pedido"
    return render_template('pedido.html', styles = styles)










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












if __name__ == '__main__':
    app.run(port = 3000, debug = True)