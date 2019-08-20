from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = b'A\x94\xe7\xd8z\xd3*O\xff\xf7XR'
conn = sqlite3.connect("Cosmind.db")
c = conn.cursor()
c.execute("SELECT * FROM user")

print(c.fetchall())
conn.close()
@app.route('/')
def main():
  return render_template('index.html')

@app.route('/reg', methods=["GET","POST"])
def reg():
    return render_template('register.html')


@app.route('/register', methods=["GET","POST"])
def register():
  if request.method == "POST":
    first = request.form['firstName']
    last = request.form['lastName']
    user2 = request.form['username']
    pass2 = request.form['password']
    while True:
      with sqlite3.connect("Cosmind.db") as dtb:
        crs = dtb.cursor()
        insert_user = ("INSERT INTO user VALUES(? ,?, ?, ?)")
        crs.execute(insert_user,[(first), (last), (user2), (pass2)])
        return render_template("index.html")


@app.route('/login', methods=["GET","POST"])
def login():
  if request.method == "POST":
    user1 = request.form['username']
    pass1 = request.form['password']
    while True:
      with sqlite3.connect("Cosmind.db") as dtb:
        crs = dtb.cursor()
      find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
      crs.execute(find_user,[(user1), (pass1)])
      results = crs.fetchall()
      
      if results:
        return render_template('about.html')
      else:
        flash('Invalid Login!')
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host="localhost")
