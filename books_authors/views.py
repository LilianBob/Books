from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author
# Create your views here.
def index(request):
    return HttpResponse("we are here")