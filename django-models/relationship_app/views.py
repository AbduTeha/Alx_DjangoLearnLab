# relationship_app/views.py
from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from django.views import generic
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

# relationship_app/views.py


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})