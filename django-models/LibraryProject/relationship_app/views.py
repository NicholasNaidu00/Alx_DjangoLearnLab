from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from .models import Book, Library  # Importing both Book and Library models

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to list all books
class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'  # Default is 'object_list'

# View to display details of a specific book
class BookDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/book_detail.html'
    context_object_name = 'book'  # Default is 'object'

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)  # Assuming there's a ForeignKey relationship
        return context

# View to create a new book
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        new_book = Book(title=title, author=author)
        new_book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/create_book.html')

# View to update an existing book
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST'):
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/update_book.html', {'book': book})

# View to delete a book
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST'):
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# View to handle user registration
def register(request):
    if request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
