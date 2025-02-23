from django.urls import path
from .views import (
    list_books,  # Import list_books function-based view
    LibraryDetailView,  # Class-based view
    library_detail,  # Function-based view
    library_list,  # Function-based view
    book_detail,  # Function-based view
    add_book,  # Function-based view
    edit_book,  # Function-based view
    delete_book,  # Function-based view
    author_detail,  # Function-based view
    author_list,  # Function-based view
    librarian_detail,  # Function-based view
    librarian_list,  # Function-based view
    RegisterView,  # Class-based view
    LoginView,  # Class-based view
    LogoutView  # Class-based view
)

urlpatterns = [
    # Function-based view for listing books
    path('books/', list_books, name='list_books'),

    # Class-based view for displaying library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Function-based views for libraries
    path('libraries/', library_list, name='library_list'),

    # Function-based views for books
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),

    # Function-based views for authors
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('authors/', author_list, name='author_list'),

    # Function-based views for librarians
    path('librarian/<int:librarian_id>/', librarian_detail, name='librarian_detail'),
    path('librarians/', librarian_list, name='librarian_list'),

    # Class-based views for user authentication
    path('register/', RegisterView.as_view(), name='register'),  # Registration
    path('login/', LoginView.as_view(), name='login'),  # Login
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout
]