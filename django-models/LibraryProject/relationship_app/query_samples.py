from relationship_app.models import Library, Author, Book, User, UserProfile, Librarian

def get_library_by_name(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f'Library found: {library.name}, Location: {library.location}')
        return library
    except Library.DoesNotExist:
        print(f'No library found with the name: {library_name}')
        return None

def create_sample_data():
    # Sample data creation to test querying
    library = Library.objects.create(name='Central Library', location='Main St', description='Main city library')
    author = Author.objects.create(name='Jane Doe', bio='An acclaimed author.', date_of_birth='1980-01-01')
    book = Book.objects.create(title='Sample Book', author=author, published_date='2023-01-01', library=library)

    print(f'Created library: {library.name}')
    print(f'Created author: {author.name}')
    print(f'Created book: {book.title}')

# Example usage
if __name__ == "__main__":
    create_sample_data()  # Uncomment to create sample data before querying
    get_library_by_name('Central Library')
    get_library_by_name('Non-existing Library')  # Testing the non-existing case