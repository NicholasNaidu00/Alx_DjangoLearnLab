from django.urls import path
from .views import list_books, create_book, update_book, delete_book, register
from .views import BookListView, BookDetailView, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('books-class/', BookListView.as_view(), name='list_books_class'),  # Class-based view
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),  # Detail view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Library detail view
    path('books/create/', create_book, name='create_book'),
    path('books/update/<int:book_id>/', update_book, name='update_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
    path('register/', register, name='register'),
]