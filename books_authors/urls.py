from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('view_book/<int:book_id>', views.view_book),
    # path('add_author', views.add_author),
    path('add_book_author/<int:book_id>', views.add_book_author),
    # path('view_author', views.view_author),
    # path('add_book', views.add_book),
    # path('add_author_book', views.add_author_book),
]