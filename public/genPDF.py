from flask import redirect, url_for
from reportlab.pdfgen import canvas
from datetime import date
import random

def genPDF_carrito(carrito, totalPagar):
    hoy = date.today()
    doc = canvas.Canvas("Prueba"+ "-" + str(random.random())[-4:] + "-" + str(hoy.day) + str(hoy.month) + str(hoy.year) +".pdf")
    
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
