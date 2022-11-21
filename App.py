from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from config import config
#from flask_wtf.csrf import CSRFProte
import collections
try:
    from collections import abc
    collections.MutableMapping = abc.MutableMapping
except:
    pass
from flask_socketio import SocketIO, send

from public.User import *
from public.faqs import *
from public.ModelUser import ModelUser
from public.User import User

app = Flask(__name__)

#seguridad.....en __main__ se asigna la proteccion al iniciar
#csrf = CSRFProtect()
# MySQL conn
mysql = MySQL(app)
login_manager_app  = LoginManager(app)


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


#LOCALES######################################################################################################LOCALES
@app.route('/carrito')
@login_required
def carrito():
    return render_template('carrito.html')


#LOGIN########################################################################################################LOGIN
user_login_py(app, mysql, User, ModelUser)


#USER#########################################################################################################USER
user_user_py(app, mysql, User, ModelUser)


app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")

#@socketio.on('message')
#def handle_message(message):
#    print("Received message: " + message)
#    if message != "User connected":
#        send(message, broadcast=True)







def status_401(error):
    return redirect(url_for('login'))
def status_404(error):
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.config.from_object(config['development'])
    #csrf.init_app(app) temporalmente
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)    
    socketio.run(app)