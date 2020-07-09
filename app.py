# Imports
from flask import Flask

# initializing our app
app = Flask(__name__)
app.debug = True

# Configs
# Our database configurations will go here

# Modules
# SQLAlchemy will be initiated here

# Models
# Our relations will be setup here

# Schema Objects
# Our schema objects will go here

# Routes
# Our GraphQL route will go here

@app.route('/')
def index():
    return 'Welcome to Book Store Api'
if __name__ == '__main__':
     app.run()