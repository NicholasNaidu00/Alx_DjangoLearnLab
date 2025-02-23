from django.urls import path
from .views import list_books, create_book, update_book, delete_book, register
from .views import BookListView, BookDetailView, LibraryDetailView

urlpatterns = [
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for listing all books
    path('books-class/', BookListView.as_view(), name='list_books_class'),
    
    # Detail view for a specific book
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
    
    # Detail view for a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Function-based view to create a new book
    path('books/create/', create_book, name='create_book'),
    
    # Function-based view to update an existing book
    path('books/update/<int:book_id>/', update_book, name='update_book'),
    
    # Function-based view to delete a specific book
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
    
    # Function-based view for user registration
    path('register/', register, name='register'),
]