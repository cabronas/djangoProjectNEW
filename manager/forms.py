from django.forms import *

from manager.models import Book


class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ("title", "text")
        widgets = {

        }
    # BookName = CharField(label="Book name", max_length=100)
    # BookText = CharField(label="Book text")
