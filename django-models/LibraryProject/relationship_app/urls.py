from django.urls import path
from .views import (
    list_books, 
    LibraryDetailView,  # Import LibraryDetailView
    library_detail, 
    library_list, 
    book_detail, 
    add_book, 
    edit_book, 
    delete_book, 
    author_detail, 
    author_list, 
    librarian_detail, 
    librarian_list
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
]