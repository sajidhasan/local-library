from django.contrib import admin
from catalog.models import Book, Author, Genre, BookInstance

#admin.site.register(Book)
#admin.site.register(BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    """field names to be displayed for the authors"""
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')

    """fields to be displayed while editing - which fields can be edited"""
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

"""for inline editing, cannot be done if not foreign key"""
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'display_genre')
    """for inline editing"""
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    #different sections
    fieldsets = (
        ('Book details', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
