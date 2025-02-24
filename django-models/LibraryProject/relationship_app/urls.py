from django.urls import path
from .views import (
    list_books,             # Import list_books function-based view
    LibraryDetailView,      # Class-based view for library details
    library_detail,         # Function-based view for specific library details
    library_list,           # Function-based view for listing libraries
    book_detail,            # Function-based view for specific book details
    add_book,               # Function-based view for adding a book
    edit_book,              # Function-based view for editing a specific book
    delete_book,            # Function-based view for deleting a specific book
    author_detail,          # Function-based view for specific author details
    author_list,            # Function-based view for listing authors
    librarian_detail,       # Function-based view for specific librarian details
    librarian_list,         # Function-based view for listing librarians
    RegisterView,           # Class-based view for user registration
    LoginView,              # Class-based view for user login
    LogoutView              # Class-based view for user logout
)

urlpatterns = [
    # Function-based view for listing books
    path('books/', list_books, name='list_books'),

    # Class-based view for displaying library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Other URL patterns
    path('libraries/', library_list, name='library_list'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('authors/', author_list, name='author_list'),
    path('librarian/<int:librarian_id>/', librarian_detail, name='librarian_detail'),
    path('librarians/', librarian_list, name='librarian_list'),

    # User Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),  # Registration
    path('login/', LoginView.as_view(), name='login'),          # Login
    path('logout/', LogoutView.as_view(), name='logout'),       # Logout
]