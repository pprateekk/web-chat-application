from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config['SECRET_KEY'] = '337336763979244226452948404D6251655468576D5A7134743777217A25432A'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp.db'
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
from webApplication import routes #app should be first initialized before routes.py can use it, else circular import error

with app.app_context():
    db.create_all()
