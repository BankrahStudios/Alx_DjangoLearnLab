from django.shortcuts import render, redirect, HttpResponse
from .models import Book, library, UserProfile
from django.contrib.auth.models import User
# from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import BookForm

# Create your views here.

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect()
    else:
        book_form = BookForm()

    return HttpResponse('add book')

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book_form = BookForm(request.POST, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect()
    else:
        book_form = BookForm(instance=book)
    pass
    return HttpResponse('edit book')

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect()
    pass
    return HttpResponse('delete book')


@login_required
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

class ViewLibrary(DetailView):
    model = library
    template_name = 'relationship_app/library_detail.html'

class UserCreationForm():
    form_class = UserCreationForm()
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'
    
@login_required   
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile == 'librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile == 'member'

@login_required
@user_passes_test(is_member)
def membership_dashboard(request):
    return render(request, 'relationship_app/member_view.html')