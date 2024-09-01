### Create
Command: `book = Book(title="1984", author="George Orwell", publication_year=1949); book.save()`
Expected Output: `Book object (1)` (or similar, indicating successful creation)

### Retrieve
Command: `book = Book.objects.get(title="1984"); print(book.title, book.author, book.publication_year)`
Expected Output: `1984 George Orwell 1949` (or similar, showing the details of the book)

### Update
Command: `book = Book.objects.get(title="1984"); book.title = "Nineteen Eighty-Four"; book.save()`
Expected Output: `Book object (1)` (or similar, indicating successful update)

### Delete
Command: `book = Book.objects.get(title="Nineteen Eighty-Four"); book.delete(); print(Book.objects.all())`
Expected Output: `[]` (or similar, confirming the deletion)