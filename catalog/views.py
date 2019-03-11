from django.shortcuts import render
from catalog.models import Author, Book, BookInstance, Genre

def index(request):
    num_books = Book.object.count()
    num_book_instances = BookInstance.object.count()
    num_authors = Author.object.count()
    num_avalaibale_instances = BookInstance.object.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_book_instances': num_book_instances,
        'num_authors': num_authors,
        'num_avalaibale_instances': num_avalaibale_instances
    }
    return render(render, 'index.html', context=context)
