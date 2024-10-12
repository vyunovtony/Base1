from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Book


def main_view(request):
    return redirect(reverse('books'))

def books_view(request):
    template = 'books/books_list.html'    
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def books_pub_date_view(request, pub_date):
    template = 'books/books_list_pub_date.html'
    books = Book.objects.filter(pub_date=pub_date).order_by('-pub_date')
    next_books = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date')
    prev_books = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date')
    context = {        
        'books': books,
        'next_books': next_books,
        'prev_books': prev_books,
        'current_date': pub_date
    }
    return render(request, template, context)