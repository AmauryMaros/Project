from flask import Flask, render_template, request, session
from database import games_from_db, games_name_from_db, platform_from_db, metascore_from_db, userscore_from_db, url_from_db, date_from_db

app = Flask(__name__)
app.secret_key = "secretkey"
#app.config["SESSION_COOKIE_NAME"] ="cookie"
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/", methods=['POST', 'GET'])
def index():
  session["games_name"] = games_name_from_db()
  session["games"] = games_from_db()
  session["platform"] = platform_from_db()
  session["metascore"] = metascore_from_db()
  session["userscore"] = userscore_from_db()
  session["url"] = url_from_db()
  session["date"] = date_from_db()
  return render_template('index.html',
                         games_name=session["games_name"],
                         games=session["games"],
                         platform=session["platform"],
                         metascore=session["metascore"],
                         userscore=session["userscore"],
                         url=session["url"],
                         date=session["date"])


@app.route('/choice', methods=['POST'])
def choice():
  session["game_choice"] = request.form['game_choice']
  return render_template('index.html',
                         game_choice=session["game_choice"],
                         games_name=session["games_name"],
                         games=session["games"],
                         platform=session["platform"],
                         metascore=session["metascore"],
                         userscore=session["userscore"],
                         url=session["url"],
                         date=session["date"])


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
