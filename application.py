import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from flask import Flask, render_template, request


engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind = engine))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method=='GET':
        return 'Ay shalunishka!'
    username = request.form.get('username')
    password = request.form.get('password')
    try_account = db.execute("SELECT * FROM users WHERE username=:name AND password=:password",{'name':username, 'password':password}).fetchone()

    if try_account:
        return render_template('search_page.html', username=username)
    return 'TRY AGAIN'

@app.route('/finded-books/', methods=['POST'])
def find_book():
    books=[]
    book_title = request.form.get('book_name')
    books_from_db = db.execute("SELECT * FROM books WHERE title LIKE :title;", {'title': '%'+book_title+'%'}).fetchall()
    for book in books_from_db:
        books.append(book)
    return render_template('finded-books.html', books=books)

@app.route('/finded-books/<string:isbn>')
def book(isbn):
    book = db.execute("SELECT * FROM books WHERE isbn=:isbn;", {'isbn':isbn}).fetchone()
    return render_template('book.html', book=book)

@app.route('/create-account')
def create_account():
    return render_template('create_account.html')

@app.route('/create-account/smth', methods=['POST'])
def apply_created_account():
    username = request.form.get('new_username')
    password = request.form.get('new_user_password')
    db.execute("INSERT INTO users(username, password) VALUES(:username, :password);", {'username': username, 'password':password})
    db.commit()
    return render_template('creating_account_result.html')
