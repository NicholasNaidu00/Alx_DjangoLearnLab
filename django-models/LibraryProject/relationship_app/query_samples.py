from relationship_app.models import Library, Author, Book, User, UserProfile, Librarian

def get_library_by_name(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f'Library found: {library.name}, Location: {library.location}')
        return library
    except Library.DoesNotExist:
        print(f'No library found with the name: {library_name}')
        return None

def get_books_in_library(library):
    if library:
        books = library.books.all()  # Retrieves all books related to this library
        print(f'Books in {library.name}:')
        for book in books:
            print(f' - {book.title} by {book.author.name}')
    else:
        print('No library provided to get books for.')

def get_books_by_author(author):
    if author:
        books = author.books.all()  # Retrieves all books written by this author
        print(f'Books by {author.name}:')
        for book in books:
            print(f' - {book.title} (Published on {book.published_date})')
    else:
        print('No author provided to get books for.')

def create_sample_data():
    # Sample data creation to test querying
    library = Library.objects.create(name='Central Library', location='Main St', description='Main city library')
    author = Author.objects.create(name='Jane Doe', bio='An acclaimed author.', date_of_birth='1980-01-01')
    book1 = Book.objects.create(title='Sample Book 1', author=author, published_date='2023-01-01', library=library)
    book2 = Book.objects.create(title='Sample Book 2', author=author, published_date='2023-02-01', library=library)

    print(f'Created library: {library.name}')
    print(f'Created author: {author.name}')
    print(f'Created books: {book1.title}, {book2.title}')

# Example usage
if __name__ == "__main__":
    create_sample_data()  # Uncomment to create sample data before querying
    library = get_library_by_name('Central Library')
    get_books_in_library(library)  # Get books in the specified library
    
    # If you want, you could also fetch books by a specific author
    author = Author.objects.get(name='Jane Doe')  # Make sure this author exists
    get_books_by_author(author)  # Get books written by the specified author