import sqlite3
def createTables():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  CREATE TABLE IF NOT EXISTS Users (
    User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL
    );
  """
  c.execute(SQL_statement)
  conn.commit()
  c.close()
  conn.close()
def PopulateTableUsers():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement1 = """
  INSERT INTO Users VALUES (NULL,'user','user');
  """
  SQL_statement2 = """
  INSERT INTO Users VALUES (NULL,'admin','admin');
  """
  c.execute(SQL_statement1)
  c.execute(SQL_statement2)
  conn.commit()
  c.close()
  conn.close()
  return True
def checkIfUserExists(username,password):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  SELECT * FROM Users WHERE Username = ? AND Password = ?
  """
  c.execute(SQL_statement,(username,password))
  result = c.fetchone()
  c.close()
  conn.close()
  if result == None:
    return False
  else:
    return True

def checkIfUserNExists(username):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  SELECT * FROM Users WHERE Username = ?
  """
  c.execute(SQL_statement,[username])
  result = c.fetchone()
  c.close()
  conn.close()
  if result == None:
    return False
  else:
    return True

def register(username,password):
    conn = sqlite3.connect('database.sql',timeout=10)
    c = conn.cursor()
    SQL_statement1 = """
      INSERT INTO Users VALUES (NULL,?,?);
    """
    c.execute(SQL_statement1,(username,password))
    conn.commit()
    c.close()
    conn.close()
    return True