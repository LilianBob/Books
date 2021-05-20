from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    return render(request, "index.html")

def books(request):
    return render(request, "books.html", {"books": Book.objects.all()})
def add_book(request):
    Book.objects.create(title= request.POST['title'], desc= request.POST['desc'])
    return redirect("/books")
def view_book(request, book_id):
    book = Book.objects.get(id= book_id)
    context = {
        "book": book,
        "authors": Author.objects.exclude(books__id= book_id)
    }
    return render(request, "book.html", context)

def authors(request):
    return render(request, 'authors.html', {"authors": Author.objects.all()})
def add_author(request):
    Author.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], notes= request.POST['notes'])
    return redirect("/authors")
def view_author(request, author_id):
    author = Author.objects.get(id= author_id)
    context = {
        "author": author,
        "books": Book.objects.exclude(authors__id= author_id)
    }
    return render(request, "author.html", context)

def add_book_author(request, book_id):
    book = Book.objects.get(id= book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f"/view_book/{book_id}")
def add_author_book(request, author_id):
    author = Author.objects.get(id= author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f"/view_author/{author_id}")