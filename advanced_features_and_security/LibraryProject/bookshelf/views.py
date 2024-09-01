from django.shortcuts import render,redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.db.models import Q
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data securely
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # ...
            return render(request, 'success.html')
    else:
        form = ExampleForm()
    return render(request, 'form_example.html', {'form': form})

def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'book_list.html', {'books': books})



# ...

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book_view(request):
    if request.method == 'POST':
        # Create book logic here
        pass
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book_view(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # Edit book logic here
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book_view(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list_view')
