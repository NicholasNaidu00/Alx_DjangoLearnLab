from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register,
    user_login,
    user_logout,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book
)

urlpatterns = [
    # URL for listing all books
    path('books/', list_books, name='list_books'),
    
    # URL for specific library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # URL for user registration
    path('register/', register, name='register'),

    # URL for user login
    path('login/', user_login, name='login'),

    # URL for user logout
    path('logout/', user_logout, name='logout'),

    # URL for admin view (restricted to Admin role)
    path('admin-view/', admin_view, name='admin_view'),

    # URL for librarian view (restricted to Librarian role)
    path('librarian-view/', librarian_view, name='librarian_view'),

    # URL for member view (restricted to Member role)
    path('member-view/', member_view, name='member_view'),

    # URL for adding a book (requires permission)
    path('add-book/', add_book, name='add_book'),

    # URL for editing a book (requires permission)
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),

    # URL for deleting a book (requires permission)
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
]