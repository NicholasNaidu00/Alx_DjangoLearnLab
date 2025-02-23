from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Library, UserProfile

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role='Member')  # Default role
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_books')
        else:
            return HttpResponse("Invalid login details.")
    return render(request, 'login.html')

# User logout view
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

# Admin view
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    # Admin-specific logic goes here
    return render(request, 'admin_view.html')  # Placeholder for admin view

# Librarian view
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    # Librarian-specific logic goes here
    return render(request, 'librarian_view.html')  # Placeholder for librarian view

# Member view
@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    # Member-specific logic goes here
    return render(request, 'member_view.html')  # Placeholder for member view

# Adding book view with permission check
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        # Logic for adding a book would go here
        pass
    return render(request, 'add_book.html')  # Placeholder for add book view

# Edit book view with permission check
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Logic for editing the book would go here
        pass
    return render(request, 'edit_book.html', {'book': book})  # Placeholder for edit book view

# Delete book view with permission check
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'delete_book.html', {'book': book})  # Placeholder for delete book view