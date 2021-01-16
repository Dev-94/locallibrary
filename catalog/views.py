from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


class BookDetailView(generic.DetailView):
    model = Book


class BookListView(generic.ListView):
    model = Book
    # # your own name for the list as a template variable
    # context_object_name = 'my_book_list'
    # # Get 5 books containing the title war, below is same as following
    # # def get_queryset(self):
    # # return Book.objects.filter(title__icontains='war')[:5]
    # queryset = Book.objects.filter(title__icontains='war')[: 5]
    # # Specify your own template name/location
    # template_name = 'books/my_arbitrary_template_name_list.html'


def index(request):

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
