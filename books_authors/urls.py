from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('add_book', views.add_book),
    path('view_book/<int:book_id>', views.view_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('add_book_author/<int:book_id>', views.add_book_author),
    path('view_author/<int:author_id>', views.view_author),
    path('add_author_book/<int:author_id>', views.add_author_book)
]