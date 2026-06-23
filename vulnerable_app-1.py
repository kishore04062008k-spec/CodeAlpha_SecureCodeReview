from flask import Flask, request, session, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "myapp123"

def setup():
    con = sqlite3.connect("mydb.db")
    con.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    con.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin123')")
    con.execute("INSERT OR IGNORE INTO users VALUES (2, 'kishore', 'kishore123')")
    con.commit()
    con.close()

@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        con = sqlite3.connect("mydb.db")
        result = con.execute("SELECT * FROM users WHERE username='" + u + "' AND password='" + p + "'").fetchone()
        con.close()
        if result:
            session["user"] = u
            return redirect("/welcome")
        else:
            msg = "Wrong username or password!"
    return f"""
    <html>
    <body>
        <h2>Login Page</h2>
        <form method="post">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
        <p style="color:red">{msg}</p>
    </body>
    </html>
    """

@app.route("/welcome")
def welcome():
    if "user" not in session:
        return redirect("/")
    return f"""
    <html>
    <body>
        <h2>Welcome {session["user"]}!</h2>
        <p>You have successfully logged in.</p>
        <a href="/logout">Logout</a>
    </body>
    </html>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

setup()
app.run(debug=True)
