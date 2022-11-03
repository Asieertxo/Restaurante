from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required


def user_login_py(app, mysql, User, ModelUser):


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User(0, request.form['name'], None, None, None, None, None, request.form['pass'])
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
    


    @app.route('/logout')
    def logout():
        logout_user()
        return render_template('index.html')