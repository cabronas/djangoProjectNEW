from django.contrib import admin
from django.urls import path, include

from manager.views import BookView

urlpatterns = [
    path('', BookView.as_view())
]
