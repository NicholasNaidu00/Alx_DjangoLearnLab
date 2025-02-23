from relationship_app.models import Book, Author, Library

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def librarian_of_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.librarian