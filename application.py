from flask import Flask, render_template, request

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

    if username == 'Advel' and password == '123':
        return render_template('search_page.html', username=username)
    return 'TRY AGAIN'

@app.route('/finded-books/', methods=['POST'])
def find_book():
    books=[]
    book = request.form.get('book_name')
    books.append(book)
    return render_template('finded-books.html', books=books)

@app.route('/finded-books/<string:book>')
def book(book):
    return book
