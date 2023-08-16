import sqlite3

connect = sqlite3.connect('books.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              author TEXT,
              year INTEGER)''')


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print("Книга: {self.title}, Автор:{self.author}, Год:{self.year}")

books = [
    ('Qwerty', 'Cvbnm', 1999),
    ('Sdfgh', 'Tyuio', 2000),
    ('Asert', 'Erfvbn', 2005)
]

cursor.executemany('INSERT INTO Books (title, author, year) VALUES (?, ?, ?)', books)
connect.commit()

cursor.execute('SELECT * FROM Books')
for row in cursor.fetchall():
    book = Book(row[1], row[2], row[3])
    book.display_info()

connect.close() 

def display_books():
    
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    
    if len(books) == 0:
        print("В базе данных нет книг")
    else:
        print("Список книг:")
        for book in books:
            print("Название: {}, Автор: {}, Год издания: {}".format(book[0], book[1], book[2]))

def add_book(title, author, year):
    
    cursor.execute("INSERT INTO books VALUES (?, ?, ?)", (title, author, year))
    connect.commit()    

def update_book(title, author=None, year=None):
    
    if author is not None:
        cursor.execute("UPDATE books SET author = ? WHERE title = ?", (author, title))
    if year is not None:
        cursor.execute("UPDATE books SET year = ? WHERE title = ?", (year, title))
    connect.commit()

def delete_book(title):
    
    cursor.execute("DELETE FROM books WHERE title = ?", (title,))
    connect.commit()


display_books()

add_book("Xbvnc", "Mnbfhtr", 1869)
add_book("Qwertyu", "Mnbfhtr", 1877)

update_book("Qwertyu", author="Mnbfhtr")
update_book("Qwertyu", year=1878)

delete_book("Xbvnc")

display_books() 
connect.commit()
connect.close() 