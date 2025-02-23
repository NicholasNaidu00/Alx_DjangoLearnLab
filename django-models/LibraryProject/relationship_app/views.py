# LibraryProject/relationship_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Book  # Assuming you have a Book model defined in models.py

# View to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/book_list.html', {'books': books})

# View to display details of a specific book
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Get the book or return 404 if not found
    return render(request, 'relationship_app/book_detail.html', {'book': book})

# View to create a new book
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        # Add other fields as applicable
        new_book = Book(title=title, author=author)  # Assuming your Book model has title and author fields
        new_book.save()  # Save the new book to the database
        return redirect('list_books')  # Redirect to the book list after creation
    return render(request, 'relationship_app/create_book.html')  # Render the book creation form

# View to update an existing book
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Get the book or return 404 if not found
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        # Update other fields as needed
        book.save()  # Save changes to the book
        return redirect('list_books')  # Redirect to book list after update
    return render(request, 'relationship_app/update_book.html', {'book': book})  # Render the update form

# View to delete a book
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Get the book or return 404 if not found
    if request.method == 'POST':
        book.delete()  # Delete the book from the database
        return redirect('list_books')  # Redirect to book list after deletion
    return render(request, 'relationship_app/delete_book.html', {'book': book})  # Render delete confirmation

# View to handle user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in immediately after registration
            return redirect('list_books')  # Redirect to the book list after successful registration
    else:
        form = UserCreationForm()  # Create an empty form if the request is not POST
    return render(request, 'relationship_app/register.html', {'form': form})  # Provide the form to the template