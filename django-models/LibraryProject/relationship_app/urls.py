from django.urls import path
from .views import list_books, BookListView, BookDetailView, LibraryDetailView, create_book, update_book, delete_book, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/list/', BookListView.as_view(), name='book_list_class'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('book/create/', create_book, name='create_book'),
    path('book/update/<int:book_id>/', update_book, name='update_book'),
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),
    path('register/', register, name='register'),
]
