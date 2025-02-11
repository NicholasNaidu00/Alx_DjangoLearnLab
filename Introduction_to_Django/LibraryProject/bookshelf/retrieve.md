# Retrieve
```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Expected Output: 1984 George Orwell 1949


#### Update the Book Title
```python
# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
