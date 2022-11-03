from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date
import base64


def user_login_py(app, mysql, User, ModelUser):


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User(0, request.form['name'].lower(), None, None, None, None, None, request.form['pass'])
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
    


    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            conn = mysql.connection.cursor()
            sql = "SELECT nombre FROM users"
            conn.execute(sql)
            nombres = conn.fetchall()

            exist = False
            for nombre in nombres:
                separador = " "  # Transformar las tuplas devueltas en cadenas para poder comparar bien los strings
                nombre = separador.join(str(parte) for parte in nombre)

                if(nombre == request.form['nombre'].lower()):
                    exist = True
                    break
                else:
                    exist = False
            
            foto = request.files['foto']
            print(foto)
            b64_foto = base64.b64encode(foto.read())
            print(b64_foto)

            if (exist):
                flash('el nombre de usuario ya existe')
                return redirect(url_for('login'))
            else:
                passw = generate_password_hash(request.form['passw'])
                conn = mysql.connection.cursor()
                conn.execute('INSERT INTO users (nombre, apellido, email, nacimiento, registro, foto, pass) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                (request.form['nombre'].lower(), request.form['apellido'].lower(), request.form['email'], request.form['nacimiento'], date.today(), b64_foto, passw))
                mysql.connection.commit()
                return redirect(url_for('carta'))
            
        else:
            return render_template('register.html')



    @app.route('/logout')
    def logout():
        logout_user()
        return render_template('index.html')