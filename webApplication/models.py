from webApplication import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length = 30), unique=True, nullable=False)
    email = db.Column(db.String(length = 40), unique = True, nullable = False)
    password = db.Column(db.String(length=50), nullable = False)
    