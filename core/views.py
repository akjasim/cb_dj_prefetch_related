from django.shortcuts import render
from core.models import Store, Book


def home(request):
    books = Book.objects.all().prefetch_related('store_set')
    for book in books:
        print(book.store_set.all())
    return None
