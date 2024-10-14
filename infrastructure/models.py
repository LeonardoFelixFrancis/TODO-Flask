from infrastructure.database import db

class Session(db.Model):

    __tablename__ = 'session'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    access_token = db.Column(db.String(50), nullable=False)
    created_date = db.Column(db.DateTime())
    minutes_alive = db.Column(db.Integer())

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Task(db.Model):

    __tablename__ = 'task'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(55), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
