from django.contrib.auth.models import User
from django.core.management import BaseCommand

from manager.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        u = User(username="Pony", password='1234')
        u.save()
        book = Book(title="book1", text="test")
        book.save()
        book.author.add(u)
        book.save()
