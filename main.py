from flask import Flask, render_template, request, redirect, url_for, jsonify
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
      return render_template('mainpage.html')
    else:
      return render_template('login.html')





@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')
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

@app.route('/radoshatelpa')
def radoshatelpa():
  return render_template("radosha-telpa.html")

@app.route('/liderusaraksts')
def liderusaraksts():
  return render_template("lideru-saraksts.html")

@app.route('/parmums')
def parmums():
  return render_template("par-mums.html")

#eksperiments:
@app.route('/aplikacija')
def aplikacija():
  return render_template("aplikacija.html")




@app.route('/teorija-uzdevums')
def teorija_uzdevums():
    return render_template("teorija-uzdevums.html")


@app.route('/load_content_1', methods=['GET'])
def load_content_1():
    with open('templates/teorija-uzd1.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})


@app.route('/load_content_2', methods=['GET'])
def load_content_2():
    with open('templates/teorija-uzd2.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})

@app.route('/load_content_3', methods=['GET'])
def load_content_3():
    with open('templates/teorija-uzd3.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})

@app.route('/load_content_4', methods=['GET'])
def load_content_4():
    with open('templates/teorija-uzd4.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})


@app.route('/load_content_5', methods=['GET'])
def load_content_5():
    with open('templates/teorija-uzd5.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})


@app.route('/load_content_6', methods=['GET'])
def load_content_6():
    with open('templates/teorija-uzd6.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})


@app.route('/load_content_7', methods=['GET'])
def load_content_7():
    with open('templates/teorija-uzd7.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})


@app.route('/load_content_8', methods=['GET'])
def load_content_8():
    with open('templates/teorija-uzd8.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})


@app.route('/load_content_9', methods=['GET'])
def load_content_9():
    with open('templates/teorija-uzd9.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})


@app.route('/load_content_10', methods=['GET'])
def load_content_10():
    with open('templates/teorija-uzd-finish.html', 'r') as file:
        content = file.read()
    return jsonify({'content': content})


@app.route('/mainpage1', methods=['GET'])
def mainpage1():
    with open('templates/mainpage1', 'r') as file:
        content = file.read()
    return jsonify({'content': content})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)