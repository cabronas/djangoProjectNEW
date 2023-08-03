from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    title = models.CharField(max_length=100, verbose_name='Book title')
    text = models.TextField(verbose_name='Book text')
    date = models.DateTimeField(auto_now=True, verbose_name='Addition date')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(verbose_name='Comment text')
    date = models.DateTimeField(auto_now=True, verbose_name='Comment date')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.book.title + " comment " + str(self.id)
