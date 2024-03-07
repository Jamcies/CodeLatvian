from flask import Flask, render_template, request, redirect, url_for
import dbMethods
import hashlib
app = Flask('app')
@app.route('/',methods=["GET","POST"])
def login():
  #dbMethods.createTables()
  #dbMethods.PopulateTableUsers()
  if request.method == 'GET':
    return render_template('login.html')
  if request.method == 'POST':
    username = request.form['username']
    passwd = request.form['password']
    passwd2 = hashlib.sha256(passwd.encode())
    password = passwd2.hexdigest()
    userExists = dbMethods.checkIfUserExists(username, password)
    if userExists:
      return redirect(url_for('mainpage'))
    else:
      return render_template('login.html')
@app.route('/mainpage',methods=["GET","POST"])
def mainpage():
    return render_template("mainpage.html")
@app.route('/register',methods=["GET","POST"])
def register():
  if request.method == 'GET':
    return render_template("register.html")
  else:
    username = request.form['username']
    passwd = request.form['password']
    passwd2 = hashlib.sha256(passwd.encode())
    password = passwd2.hexdigest()
    userNameExists = dbMethods.checkIfUserNExists(username)
    if userNameExists:
      return redirect(url_for('login'))
    else:
      username = request.form['username']
      passwd = request.form['password']
      passwd2 = hashlib.sha256(passwd.encode())
      password = passwd2.hexdigest()
      dbMethods.register(username,password)
      return redirect("mainpage")


@app.route('/teorija')
def teorija():
  return render_template("teorija-uzd.html")

@app.route('/teorija1')
def teorija1():
  return render_template("teorija-uzd1.html")

@app.route('/teorija2')
def teorija2():
  return render_template("teorija-uzd2.html")

@app.route('/teorija3')
def teorija3():
  return render_template("teorija-uzd3.html")

@app.route('/teorija4')
def teorija4():
  return render_template("teorija-uzd4.html")

@app.route('/teorija5')
def teorija5():
  return render_template("teorija-uzd5.html")

@app.route('/teorija6')
def teorija6():
  return render_template("teorija-uzd6.html")

@app.route('/teorija7')
def teorija7():
  return render_template("teorija-uzd7.html")

@app.route('/teorija8')
def teorija8():
  return render_template("teorija-uzd8.html")

@app.route('/teorijafinish')
def teorijafinish():
  return render_template("teorija-uzd-finish.html")

@app.route('/mainpagepabeigts')
def jaunsmainpage():
  return render_template("index-jauns.html")

@app.route('/radoshatelpa')
def radoshatelpa():
  return render_template("radosha-telpa.html")

@app.route('/liderusaraksts')
def liderusaraksts():
  return render_template("lideru-saraksts.html")

@app.route('/parmums')
def parmums():
  return render_template("par-mums.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
