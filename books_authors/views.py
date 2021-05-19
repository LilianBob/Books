from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    return render(request, "index.html", {"books": Book.objects.all()})
def add_book(request):
    Book.objects.create(title= request.POST['title'], desc= request.POST['desc'])
    return redirect("/")
# def view_book(request):
#     book = Book.objects.get(id= book_id)
#     context = {
#         "book": book,
#         "authors": Author.objects.exclude(books__id= book_id)
#     }
#     return render(request,'book.html', context)