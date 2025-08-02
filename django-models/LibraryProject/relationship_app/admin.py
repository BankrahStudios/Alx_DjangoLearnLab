from django.contrib import admin
from .models import Author, Book, UserProfile, library

# Register your models here.

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'published_date')
#     search_fields = ('title', 'author')

# admin.site.register(BookAdmin)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(library)