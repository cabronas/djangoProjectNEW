from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.messages.context_processors import messages
from django.db.models import Count, Prefetch
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from manager.forms import *
from manager.models import Book, Comment


# Create your views here.
class BooksView(View):
    def get(self, request):
        data = {'Books': Book.objects.all().prefetch_related('author')}
        return render(request, 'Book view.html', context=data)


class BookView(View):
    def get(self, request, book_id):
        # if not request.session.has_key('book_id'):
        #     request.session['book_id'] = request.GET['BookButton']
        # try:
        #     if request.session['book_id'] != request.GET['BookButton']:
        #         request.session['book_id'] = request.GET['BookButton']
        # except:
        #     pass

        book = Book.objects.filter(id=book_id).prefetch_related('author').all()
        comment = Comment.objects.filter(book_id=book_id).select_related(
            'user').annotate(likes_comments=Count('likes'))
        data = {'Book': book[0],
                'Comments': comment}
        return render(request, 'ViewBook.html', context=data)


class AddLikeView(View):
    def get(self, request, book_id):
        if request.user.is_authenticated:
            book = Book.objects.get(id=book_id)
            if request.user not in book.likes.all():
                book.likes.add(request.user)
                book.likes_count += 1
            else:
                book.likes.remove(request.user)
                book.likes_count -= 1
            book.save()
        return redirect("BookView", book_id)


class Return_To_Menu(View):
    def get(self, request):
        return redirect("menu")


class DeleteBook(View):
    def get(self, request, book_id):
        if request.user.is_authenticated:
            b = Book.objects.get(id=book_id)
            if request.user in b.author.all():
                b.delete()
            return redirect("menu")
        return redirect("menu")


class UpdateBook(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        form = {'form': AddBookForm(instance=book),
                'book': book}
        return render(request, 'UpdateBook.html', form)

    def post(self, request, book_id):
        if request.user.is_authenticated:
            b = Book.objects.get(id=book_id)
            if request.user in b.author.all():
                form = AddBookForm(data=request.POST, instance=b)
                form.save()
                return redirect("BookView", book_id=b.id)
        return redirect("menu")


class AddBookView(View):
    def get(self, request):
        form = {
            'form': AddBookForm()
        }
        return render(request, 'AddBook.html', form)

    def post(self, request):
        if request.user.is_authenticated:
            form = AddBookForm(request.POST)
            if form.is_valid():
                # data = request.POST
                book: Book = form.save()
                book.author.add(request.user)
                return redirect("BookView", book_id=book.id)
        return redirect("menu")
