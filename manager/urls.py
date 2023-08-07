from django.contrib import admin
from django.urls import path, include

from manager.views import BooksView, BookView, AddLikeView

urlpatterns = [
    path('menu', BooksView.as_view(), name=""),
    path('BookView', BookView.as_view(), name='BookView'),
    path('add_like/<int:book_id>', AddLikeView.as_view(), name='add_like'),
]
