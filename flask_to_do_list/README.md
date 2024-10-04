# Flask-To-Do-List

@freeCodeCamp - Flask tutorial

### How to run the app

### 1/ Virtual Env & package installation
```
$ pip3 install virtualenv

$ virtualenv env

$ source env/bin/activate

$ pip3 install flask flask-sqlalchemy
```
### 2/ Init the DB

Open the python3 shell :

```$ python3```

Then :

```
 >>> from app import app, db

 >>> app.app_context().push()

 >>> db.create_all()

 >>> exit()
```
### 3/ Run the app (go to localhost:5000)

```python3 app.py```
