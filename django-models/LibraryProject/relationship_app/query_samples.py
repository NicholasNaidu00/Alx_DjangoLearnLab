from relationship_app.models import Library, Author, Book, User, UserProfile, Librarian

def get_library_by_name(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f'Library found: {library.name}, Location: {library.location}')
        return library
    except Library.DoesNotExist:
        print(f'No library found with the name: {library_name}')
        return None

def get_author_by_name(author_name):
    try:
        author = Author.objects.get(name=author_name)
        print(f'Author found: {author.name}, Bio: {author.bio}')
        return author
    except Author.DoesNotExist:
        print(f'No author found with the name: {author_name}')
        return None

def get_librarian_by_library(library):
    if library:
        try:
            librarian = Librarian.objects.get(library=library)  # Find librarian for the specific library
            print(f'Librarian found: {librarian.user.username} (works at: {library.name})')
            return librarian
        except Librarian.DoesNotExist:
            print(f'No librarian found for the library: {library.name}')
            return None
    else:
        print('No library provided to get librarian for.')
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
        books = Book.objects.filter(author=author)  # Retrieves all books written by this author
        print(f'Books by {author.name}:')
        for book in books:
            print(f' - {book.title} (Published on {book.published_date})')
    else:
        print('No author provided to get books for.')

def create_sample_data():
    # Sample data creation to test querying
    library = Library.objects.create(name='Central Library', location='Main St', description='Main city library')
    author = Author.objects.create(name='Jane Doe', bio='An acclaimed author.', date_of_birth='1980-01-01')
    librarian_user = User.objects.create(username='librarian_jane', password='password')
    librarian = Librarian.objects.create(user=librarian_user, library=library)
    
    book1 = Book.objects.create(title='Sample Book 1', author=author, published_date='2023-01-01', library=library)
    book2 = Book.objects.create(title='Sample Book 2', author=author, published_date='2023-02-01', library=library)

    print(f'Created library: {library.name}')
    print(f'Created author: {author.name}')
    print(f'Created librarian: {librarian.user.username} for {library.name}')
    print(f'Created books: {book1.title}, {book2.title}')

# Example usage
if __name__ == "__main__":
    create_sample_data()  # Uncomment to create sample data before querying
    library = get_library_by_name('Central Library')
    get_books_in_library(library)  # Get books in the specified library

    author = get_author_by_name('Jane Doe')  # Get the author by name
    get_books_by_author(author)  # Get books written by the specified author
    
    get_librarian_by_library(library)  # Get librarian for the specified library