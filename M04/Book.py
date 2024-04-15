#Kesny Raingsey
#4/15/2024
#Book.py

from flask import Flask, request


#__name__means whatever the name of the file I am in (in our case application.py)
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    #create a table for drink. That table will have an ID, name, and a description(3 fields0. each one will have a data type (int, sting, etc..) and any other type of options we need to add.
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))
    
    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"
#define some routes... routes are URLS that are tied to functions (simple definition)
@app.route('/')
def index():
    return 'Welcome!'

#route that grabs all the drinks

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {"drinks" : output}
    
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book= Book(book_name=request.json['book_name'],
                  author=request.json['author'],
                  publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!@"}
