from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from config import config
#from flask_wtf.csrf import CSRFProte
import collections
import json
try:
    from collections import abc
    collections.MutableMapping = abc.MutableMapping
except:
    pass
from flask_socketio import SocketIO, send
from reportlab.pdfgen import canvas

from public.User import *
from public.faqs import *
from public.ModelUser import ModelUser
from public.User import User
from public.chatbot import Chatbot

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

@app.route('/savecarrito', methods=['POST'])
@login_required
def savecarrito():
    c = canvas.Canvas("Prueba.pdf")
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30,750, "ASIER BURGER`S")
    c.setFont("Helvetica", 10)
    c.drawString(30,730, "Las Rozas de Madrid, Madrid")
    c.drawString(30,710, "Telefono: 901142536")
    c.drawString(30,690, "Fax: 654844963")

    c.setFont("Helvetica-Bold", 10)
    c.drawString(30,660, "Para:")
    c.setFont("Helvetica", 10)
    c.drawString(30,640, "Nombre: Asier Garcia")
    c.drawString(30,620, "Email: asier@gmail.com")
    c.drawString(30,600, "Telefono: 644355874")
    c.drawString(30,580, "Direccion: Calle de al lado")
    c.drawString(30,560, "Ciudad, CP: Las Rozas de Madrid, 28231")
    c.drawString(30,540, "Telefono: 644355847")

    c.setFont("Helvetica-Bold", 10)
    c.drawString(30,510, "Comentarios o instrucciones especiales:")


    c.save()

    return redirect(url_for('carrito'))


#LOGIN########################################################################################################LOGIN
user_login_py(app, mysql, User, ModelUser)


#USER#########################################################################################################USER
user_user_py(app, mysql, User, ModelUser)


app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    if message != "User connected":
        send(Chatbot(message), broadcast=True)







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