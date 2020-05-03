import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))

db = scoped_session(sessionmaker(bind = engine))


#db.execute("CREATE TABLE users(id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL);")

db.execute("CREATE TABLE books(isbn VARCHAR PRIMARY KEY, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year INTEGER NOT NULL);")
#db.execute("INSERT INTO users(username, password) VALUES(:username, :password);", {'username':'VLask', 'password': '132'})

db.commit()
