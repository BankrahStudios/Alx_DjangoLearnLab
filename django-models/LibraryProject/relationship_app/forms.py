from django import forms
from .models import UserProfile, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']