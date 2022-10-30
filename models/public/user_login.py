from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from datetime import date


def user_login_py(app, mysql, User, ModelUser):


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User(0, request.form['name'], request.form['pass'])
            logged_user = ModelUser.login(mysql, user)
            
            if logged_user != None:
                print(logged_user.password)
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

                if(nombre == request.form['nombre']):
                    exist = True
                    break
                else:
                    exist = False
            
            print(exist)        
            if (exist):
                flash('el nombre de usuario ya existe')
                return redirect(url_for('login'))
            else:
                passw = generate_password_hash(request.form['passw'])
                conn = mysql.connection.cursor()
                conn.execute('INSERT INTO users (nombre, apellido, email, nacimiento, registro, pass) VALUES (%s, %s, %s, %s, %s, %s)',
                (request.form['nombre'], request.form['apellido'], request.form['email'], request.form['nacimiento'], date.today(), passw))
                mysql.connection.commit()
                return redirect(url_for('carta'))
            
        else:
            return render_template('register.html')
    

    @app.route('/logout')
    def logout():
        logout_user()
        return render_template('index.html')