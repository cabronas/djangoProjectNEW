from django.shortcuts import render
from django.views import View

from manager.models import Book


# Create your views here.
class BookView(View):
    def get(self, request):
        data = {'Books': Book.objects.all()}
        return render(request, 'Book view.html', context=data)
