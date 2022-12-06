from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from config import config
#from flask_wtf.csrf import CSRFProte
from flask_socketio import SocketIO, send
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import json


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
    carrito = request.form['carrito']
    carrito = json.loads(carrito)
    totalPagar = request.form['totalPagar']
    totalPagar = json.loads(totalPagar)
    
    doc = canvas.Canvas("Prueba.pdf")
    
    doc.setFont("Helvetica-Bold", 20)
    doc.drawString(30,750, "ASIER BURGER`S")
    doc.setFont("Helvetica", 10)
    doc.drawString(30,730, "Las Rozas de Madrid, Madrid")
    doc.drawString(30,710, "Telefono: 901142536")
    doc.drawString(30,690, "Fax: 654844963")

    doc.setFont("Helvetica-Bold", 10)
    doc.drawString(30,660, "Para:")
    doc.setFont("Helvetica", 10)
    doc.drawString(30,640, "Nombre: Asier Garcia")
    doc.drawString(30,620, "Email: asier@gmail.com")
    doc.drawString(30,600, "Telefono: 644355874")
    doc.drawString(30,580, "Direccion: Calle de al lado")
    doc.drawString(30,560, "Ciudad, CP: Las Rozas de Madrid, 28231")
    doc.drawString(30,540, "Telefono: 644355847")
    
    doc.setFont("Helvetica-Bold", 10)
    doc.drawString(30,510, "Cantidad")
    doc.drawString(100,510, "Producto")
    doc.drawString(400,510, "Precio U.")
    doc.drawString(450,510, "Precio T.")
    doc.line(30,505,500,505)
    
    y = 470
    precioTotal = 0
    doc.setFont("Helvetica", 8)
    for item in carrito:
        price = float(item['price'][:-1])
        doc.drawString(30, y, str(item['cant']))
        doc.drawString(100, y, item['name'])
        doc.drawString(420, y, str(price))
        doc.drawString(470, y, str(round(price * int(item['cant']), 2)))
        y = y - 7
        doc.line(30,y,500,y)
        y = y - 13
        precioTotal = round(precioTotal + price * int(item['cant']), 2)
       
    doc.drawString(370, y, "Subtotal")
    doc.drawString(470, y, str(round(totalPagar['subtotal'] * 0.9, 2)))
    doc.line(370,y-2,500,y-2)
    doc.drawString(370, y-20, "I.V.A.(10%)")
    doc.drawString(470, y-20, str(round(totalPagar['total'] * 0.1, 2)))
    doc.line(370,y-22,500,y-22)
    doc.drawString(370, y-40, "Servicio")
    doc.drawString(470, y-40, str(round(totalPagar['servicio'], 2)))
    doc.line(370,y-42,500,y-42)
    doc.drawString(370, y-60, "Transporte")
    doc.drawString(470, y-60, str(round(totalPagar['transporte'], 2)))
    doc.line(370,y-62,500,y-62)
    doc.drawString(370, y-80, "Descuento")
    doc.drawString(470, y-80, str(round(totalPagar['descuento'], 2)))
    doc.line(370,y-82,500,y-82)
    doc.drawString(370, y-100, "Total")
    doc.drawString(470, y-100, str(round(totalPagar['total'], 2)))

    doc.save()


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