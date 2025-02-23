# relationship_app/query_samples.py
import os
import django

# Here 'django_models' should match the name of your project folder
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian