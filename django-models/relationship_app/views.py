# relationship_app/views.py
from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from django.views import generic
from .models import Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
    return render(request, 'relationship_app/list_books.html')



def library_detail(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/library_detail.html')
class LibraryDetailView(generic.DetailView):
    model = Library
    template_name = 'library_detail.html'

   