from django.contrib import admin
from catalog.models import Book, Author, Genre, BookInstance

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Author)
