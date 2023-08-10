from django.contrib import admin
from django.urls import path, include

from manager.views import BooksView, BookView, AddLikeView, Return_To_Menu

urlpatterns = [
    path('menu', BooksView.as_view(), name="menu"),
    path('BookView/<int:book_id>', BookView.as_view(), name='BookView'),
    path('add_like/<int:book_id>', AddLikeView.as_view(), name='add_like'),
    path('return_to_menu', Return_To_Menu.as_view(), name='return_to_menu'),
]
