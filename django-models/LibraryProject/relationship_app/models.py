from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    class Meta:
        permissions = (
            ('can_add_book', 'Can Delete Book'),
            ('can_change_book', 'Can Change Book'),
            ('can_delete_book', 'Can Delete Book')
        )

    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    Library = models.OneToOneField('Library', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('librarian', 'Librarian'), ('member', 'Member')])

    # def __str__(self):
    #     return self.user
