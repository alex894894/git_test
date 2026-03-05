from django.shortcuts import render
from . import models

def book_list(request):
    books=models.Books.objects.all()
    return render(request, "books.html" , {'books':books})
