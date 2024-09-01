### Delete
Command: `book = Book.objects.get(title="Nineteen Eighty-Four"); book.delete(); print(Book.objects.all())`
Expected Output: `[]` (or similar, confirming the deletion)