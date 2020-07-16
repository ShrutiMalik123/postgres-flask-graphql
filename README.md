# postgres-flask-graphql

### My flask and graphQL project with PostgreSQL

### py -m venv env

### .\env\Scripts\activate

### To start SQL shell . Enter all the necessary information such as the server, database, port, username, and password. To accept the default, you can press Enter. Note that you should provide the password that you entered during installing the PostgreSQL. Lastly issue the command SELECT version();

### my username is postgres

### my password is password

### the IP address is localhost (127.0.0.1)

### the port is 5432

### the database name is book-store-api

### 'postgresql://postgres:password@localhost:5432/book-store-api'

### pip install flask flask-graphql flask-migrate sqlalchemy graphene graphene-sqlalchemy psycopg2-binary

### Now let’s create some demo data. Type python from the terminal. and execute the following code line by line

### >>> from app import db, User, Book

### >>> postgres = User(username='postgresuser', email='email@gmail.com')

### >>> db.session.add(postgres)

### >>> db.session.commit()

### >>> flaskbook = Book()

### >>> flaskbook.title = "Building with Flask"

### >>> flaskbook.description = "The best Flask Python book on the web"

### >>> flaskbook.year = 2020

### >>> flaskbook.author_id = postgresisscary.id

### >>> db.session.add(flaskbook)

### >>> db.session.commit()

### if error: >>> db.session.rollback()
