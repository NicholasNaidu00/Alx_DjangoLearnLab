
#### Update the Book Title
```python
# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)


#### Delete the Book
```python
# Delete the book
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)
