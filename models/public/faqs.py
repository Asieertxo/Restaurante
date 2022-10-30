from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date


def faqs_py(app, mysql):


    @app.route('/faqs')
    def faqs():
        conn = mysql.connection.cursor()
        conn.execute('SELECT * FROM faqs')
        faqs = conn.fetchall()
        return render_template('faqs.html',faqs = faqs)


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


    @app.route('/añadir_comentario', methods=['POST'])
    def añadir_comentario():
            if request.method == 'POST':
                nombre = request.form['nombre']
                apellido = request.form['apellido']
                email = request.form['email']
                mensaje = request.form['mensaje']
                likes = 0
                fecha = date.today()

                conn = mysql.connection.cursor()
                conn.execute('INSERT INTO faqs (nombre, apellido, email, mensaje, likes, fecha) VALUES (%s, %s, %s, %s, %s, %s)',
                (nombre, apellido, email, mensaje, likes, fecha))
                flash('Pregunta guardada')
                mysql.connection.commit()

                return redirect(url_for('faqs'))