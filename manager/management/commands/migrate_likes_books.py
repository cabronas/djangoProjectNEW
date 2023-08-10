from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db.models import Count

from manager.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        books = Book.objects.annotate(book_likes=Count('likes'))
        for book in books:
            book.likes_count = book.book_likes
        Book.objects.bulk_update(books, ['likes_count'], batch_size=255)
        # books.save()
