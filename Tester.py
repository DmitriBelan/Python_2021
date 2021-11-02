from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "helloworld"
app.permanent_session_lifetime = timedelta(seconds=2)

@app.route("/")
def home():
    title = 'Hello world'
    people = ['Bob', 'Mary', 'Jack']
    return render_template('home.html', mytitle=title, people=people)

@app.route("/login", methods = ['POST','GET'])
def login():

    if request.method == 'POST':
        session.permanent = True
        user_name = request.form['nm']
        session['user'] = user_name
        return render_template('user.html', usr=user_name)


    return render_template('Login.html')

@app.route("/user")
def user():
    if 'user' in session:
        user_name = session['user']
        return render_template('user.html', usr=session['user'])
    else:
        return redirect(url_for('login'))
@app.route("/logout")
def logout():
    return "<p>Logout page</p>"

# Проверка на запуск только из материнского файла. Защита от воровства кода.
if __name__=='__main__':
    app.run(debug=True)
