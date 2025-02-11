# Create
```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Expected Output: <Book: 1984>


#### Retrieve the Book
```python
# Retrieve the book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
