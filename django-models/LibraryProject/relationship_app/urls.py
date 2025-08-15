from django.urls import path
from .models import Book
from . import views
from .views import list_books, UserCreationForm, add_book, edit_book, delete_book, admin_dashboard, librarian_dashboard, membership_dashboard
from . import admin_view, librarian_view, member_view
# from .admin_view import admin_dashboard
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.list_books , name='book'),
    # path('', views.current_datetime , name='time'),
    path('library/<int:pk>/', views.ViewLibrary.as_view(), name='view_library' ),
    path('accounts/login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('accounts/register/', UserCreationForm.as_view(template_name='relationship_app/register.html'), name='register'),
    path('admin-only/', views.admin_dashboard, name='admin_view'),
    path('librarian/', views.librarian_dashboard, name='librarian_view'),
    path('member/', views.membership_dashboard, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book')
]


# views.register
# LibraryDetailView