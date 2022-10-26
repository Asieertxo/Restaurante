from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from datetime import date
import os
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required

#Models y Entities
from models.ModelUser import ModelUser
from models.entities.User import User

app = Flask(__name__)

# MySQL conn
mysql = MySQL(app)
login_manager_app  = LoginManager(app)



@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql, id)



#importacion de la capeta de imagenes
picFolder = os.path.join('static', 'img')
app.config['UPLOAD_IMG'] = picFolder

##############################################################################################################HOME
@app.route('/')
def index():
    return render_template('index.html')







##############################################################################################################CARTA
@app.route('/carta')
def carta():
    conn = mysql.connection.cursor()
    conn.execute('SELECT * FROM carta')
    carta = conn.fetchall()

    #img = os.path.join(app.config['UPLOAD_IMG'], 'prueba.jpg')

    return render_template('carta.html', carta = carta)







##############################################################################################################LOCALES
@app.route('/locales')
def locales():
    return render_template('locales.html')













##############################################################################################################FAQS
@app.route('/faqs')
def faqs():



    conn = mysql.connection.cursor()
    conn.execute('SELECT * FROM faqs')
    faqs = conn.fetchall()
    return render_template('faqs.html',faqs = faqs)


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
        conn.execute('INSERT INTO faqs (nombre, apellido, email, mensaje, likes, fecha) VALUES (%s, %s, %s, %s, %s, %s)',
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








##############################################################################################################LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['name'], request.form['pass'])
        logged_user = ModelUser.login(mysql, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('index'))
            else:
                flash('Contraseña incorrecta...')
                return redirect(url_for('login'))
        else:
            flash('Usuario no encontrado...')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')


















if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()