# LibraryProject/relationship_app/urls.py
from django.urls import path
from .views import (
    list_books,
    book_detail,
    create_book,
    update_book,
    delete_book,
    register,  # Import the register view
)
from django.contrib.auth.views import LoginView, LogoutView  # For login/logout views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL to view all books
    path('books/<int:book_id>/', book_detail, name='book_detail'),  # URL to view a single book's details
    path('books/create/', create_book, name='create_book'),  # URL to create a new book
    path('books/<int:book_id>/edit/', update_book, name='update_book'),  # URL to edit a book
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),  # URL to delete a book

    path('register/', register, name='register'),  # URL for user registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login URL
    path('logout/', LogoutView.as_view(template_name='relationship_app/logged_out.html'), name='logout'),  # Logout URL
]