from django.shortcuts import render
from django.urls import reverse
from django.views import View

from manager.models import Book, Comment


# Create your views here.
class BooksView(View):
    def get(self, request):
        data = {'Books': Book.objects.all()}
        return render(request, 'Book view.html', context=data)


class BookView(View):
    def post(self, request):
        data = {'Book': Book.objects.filter(id=request.POST['BookButton']),
                'Comments': Comment.objects.filter(book_id=request.POST['BookButton'])}
        return render(request, 'ViewBook.html', context=data)


class AddLikeView(View):
    def get(self, request, book_id):
        Book.objects.get(id=book_id)
        Book.likes += 1
        return reverse('BookView')
