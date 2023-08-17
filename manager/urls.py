from django.contrib import admin
from django.urls import path, include

from manager.views import *

urlpatterns = [
    path('menu', BooksView.as_view(), name="menu"),
    path('BookView/<int:book_id>', BookView.as_view(), name='BookView'),
    path('add_like/<int:book_id>', AddLikeView.as_view(), name='add_like'),
    path('return_to_menu', Return_To_Menu.as_view(), name='return_to_menu'),
    path('add_book', AddBookView.as_view(), name='AddBook'),
    path('delete_book/<int:book_id>', DeleteBook.as_view(), name='delete_book'),
    path('update_book/<int:book_id>', UpdateBook.as_view(), name='update_book'),

]
