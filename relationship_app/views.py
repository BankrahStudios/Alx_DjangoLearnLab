from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Book
    template_name = 'library_detail.html'
