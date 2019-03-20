from django.shortcuts import render
from catalog.models import Author, Book, BookInstance, Genre

def index(request):
    num_books = Book.objects.count()
    num_book_instances = BookInstance.objects.count()
    num_authors = Author.objects.count()
    num_available_instances = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_book_instances': num_book_instances,
        'num_authors': num_authors,
        'num_available_instances': num_available_instances
    }
    return render(request, 'index.html', context=context)
