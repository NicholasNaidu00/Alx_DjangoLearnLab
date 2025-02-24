from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f'{self.user.username} ({self.role})'


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, related_name='librarians', on_delete=models.CASCADE)

    def __str__(self):
        return f'Librarian: {self.user.username} at {self.library.name}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField()
    library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Signal to automatically create or update UserProfile and Librarian
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        if instance.userprofile.role == 'Librarian':  # Automatically create a Librarian
            # Assign the librarian to the first library for simplicity
            library = Library.objects.first()
            if library:
                Librarian.objects.create(user=instance, library=library)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    # Save librarian if it exists
    if hasattr(instance, 'librarian'):
        instance.librarian.save()