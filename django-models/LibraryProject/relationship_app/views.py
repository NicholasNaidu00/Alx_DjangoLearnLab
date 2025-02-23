from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Library, Author, Book, Librarian, UserProfile
from .forms import BookForm  # Assuming you have a form for adding/editing books

# View to display details of a specific library
def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    books = Book.objects.filter(library=library)
    librarians = Librarian.objects.filter(library=library)
    
    context = {
        'library': library,
        'books': books,
        'librarians': librarians,
    }
    
    return render(request, 'relationship_app/library_detail.html', context)

# View to display a list of all libraries
def library_list(request):
    libraries = Library.objects.all()
    context = {
        'libraries': libraries,
    }
    return render(request, 'relationship_app/library_list.html', context)

# View to display details of a specific book
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'relationship_app/book_detail.html', context)

# View to add a new book (requires login)
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.library = Library.objects.first()  # Assign to the first library for simplicity
            book.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm()
    
    context = {
        'form': form,
    }
    return render(request, 'relationship_app/add_book.html', context)

# View to edit an existing book (requires login)
@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'relationship_app/edit_book.html', context)

# View to delete a book (requires login)
@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('library_list')
    
    context = {
        'book': book,
    }
    return render(request, 'relationship_app/delete_book.html', context)

# View to display details of a specific author
def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)
    
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'relationship_app/author_detail.html', context)

# View to display a list of all authors
def author_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'relationship_app/author_list.html', context)

# View to display details of a specific librarian
def librarian_detail(request, librarian_id):
    librarian = get_object_or_404(Librarian, id=librarian_id)
    context = {
        'librarian': librarian,
    }
    return render(request, 'relationship_app/librarian_detail.html', context)

# View to display a list of all librarians
def librarian_list(request):
    librarians = Librarian.objects.all()
    context = {
        'librarians': librarians,
    }
    return render(request, 'relationship_app/librarian_list.html', context)