from flask import Flask, session, request, render_template,redirect,url_for,g
import os

app=Flask(__name__)
app.secret_key = os.urandom(24)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'<User:{self.username}>'
users = []
users.append(User(id=1, username="test", password="test"))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods=["GET","POST"])
def signin():
    if request.method =='POST':
        session.pop('user_id',None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('member'))
        return redirect(url_for('error'))    
    return render_template("error.html")


@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/signout")
def signout():
    session.pop('username',None)
    return redirect(url_for('index'))
#    return render_template("index.html")
@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(port=3000)
