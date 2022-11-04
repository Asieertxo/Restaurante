from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from config import config
from flask_wtf.csrf import CSRFProtect

from models.public.user_login import *
from models.public.faqs import *
from models.public.ModelUser import ModelUser
from models.public.User import User

app = Flask(__name__)

#seguridad.....en __main__ se asigna la proteccion al iniciar
csrf = CSRFProtect()
# MySQL conn
mysql = MySQL(app)
login_manager_app  = LoginManager(app)


#importacion de la capeta de imagenes
picFolder = os.path.join('static', 'img')
app.config['UPLOAD_IMG'] = picFolder



@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql, id)











#HOME##########################################################################################################HOME
@app.route('/')
def index():
    return render_template('index.html')


#CARTA########################################################################################################CARTA
@app.route('/carta')
def carta():
    conn = mysql.connection.cursor()
    conn.execute('SELECT * FROM carta')
    carta = conn.fetchall()
    return render_template('carta.html', carta = carta)


#LOCALES######################################################################################################LOCALES
@app.route('/locales')
def locales():
    return render_template('locales.html')


#FAQS#########################################################################################################FAQS
faqs_py(app, mysql)


#LOGIN########################################################################################################LOGIN
user_login_py(app, mysql, User, ModelUser)


#USER#########################################################################################################USER
@app.route('/user')
@login_required
def user():
    return render_template('user.html')


@app.route('/borrarusuario', methods=['POST'])
@login_required
def borrarusuario():
    conn = mysql.connection.cursor()
    sql = "DELETE FROM users WHERE id = '{}'".format(request.form['id'])
    conn.execute(sql)
    mysql.connection.commit()
    return redirect(url_for('logout'))

@app.route('/cambiarcontraseña' , methods=['POST'])
@login_required
def cambiarcontraseña():
    conn = mysql.connection.cursor()
    sql = "SELECT id FROM users WHERE id = '{}'".format(request.form['id'])
    conn.execute(sql)
    row = conn.fetchone()

    print(request.form['passactual'])
    print(request.form['passactualhidden'])
    if(User.check_password(request.form['passactual'], request.form['passactualhidden'])):
        conn = mysql.connection.cursor()
        sql = 'UPDATE users SET pass = %s WHERE id = %s)',
        (request.form['passnueva'], request.form['id'])
        conn.execute(sql)
        mysql.connection.commit()
    else:
        flash('Contraseña incorrecta...')
        return redirect(url_for('user'))











def status_401(error):
    return redirect(url_for('login'))
def status_404(error):
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.config.from_object(config['development'])
    #csrf.init_app(app) temporalmente
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()