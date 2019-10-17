from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect

app = Flask(__name__)
app.config.from_pyfile('config/production.py')

#Autenticacion
# app.add_url_rule('/login', 'login', login)
# app.add_url_rule('/logout', 'auth_logout', auth.logout)
# app.add_url_rule(
#     '/authenticate',
#     'auth_authenticate',
#     auth.authenticate,
#     methods=['POST']
# )

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/login.html', methods=['POST', 'GET'])
def login():
    error = ''
    if request.method == 'POST':
        if request.form['password'] == '1234' and request.form['user'] == 'admin':
            session['logged_in'] = True
            flash('logeo exitoso!')
            return redirect(url_for('index'))
        else:
            error = 'credenciales invalidas'
    return render_template('login.html', error=error)

@app.route('/')
def logout():
    session['logged_in'] = False
    return index()

if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.secret_key = 'hola'
    app.run()