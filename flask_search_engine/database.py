from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def games_name_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT Name FROM mytable2"))
    games_name = []
    for row in result.all():
      games_name.append(row[0])
      
    return games_name
    
def platform_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT Platform FROM mytable2"))
    platform = []
    for row in result.all() :
      platform.append(row[0])
    return platform

def date_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT Date FROM mytable2"))
    date = []
    for row in result.all() :
      date.append(row[0])
    return date


def metascore_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT Metascore FROM mytable2"))
    metascore = []
    for row in result.all() :
      metascore.append(row[0])
    return metascore

def userscore_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT Userscore FROM mytable2"))
    userscore = []
    for row in result.all() :
      userscore.append(row[0])
    return userscore

def url_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT URL FROM mytable2"))
    URL = []
    for row in result.all() :
      URL.append(row[0])
    return URL


def games_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM mytable2"))
    games = []
    for row in result.all() :
      games.append(dict(zip(result.keys(), row)))
    return games

