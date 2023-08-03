from django.contrib import admin
from django.urls import path, include

from manager.views import BooksView, BookView

urlpatterns = [
    path('', BooksView.as_view()),
    path('BookView', BookView.as_view(), name='BookView'),
    # path('addlike', BookView.as_view(), name='BookView')
]
