# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initializing our app
app = Flask(__name__)
app.debug = True

# Configs
# Replace the user, password, hostname and database according to your configuration information


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:omega123@localhost:5432/book-store-api'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

# Modules
db = SQLAlchemy(app)

# Models
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    books = db.relationship('Book', backref='author')

    def __init__(self, username, email):
      self.username = username
      self.email = email

    def __repr__(self):
        return '<User %r>' % self.id

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Book %r>' % self.title % self.description % self.year % self.author_id

# Schema Objects
# Our schema objects will go here

# Routes
# Our GraphQL route will go here

@app.route('/')
def index():
    return 'Welcome to Book Store Api'
if __name__ == '__main__':
     app.run()