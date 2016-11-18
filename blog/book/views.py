from django.shortcuts import render
from book.models import Book

def book(request):
    '''
    Render the article page
    '''
    books = Book.objects.all()
    itemsList = []
    for book in books:
        items = [book]
        itemsList.append(items)
    context = {'itemsList':itemsList}
    return render(request, 'book/book.html', context)
# Create your views here.

