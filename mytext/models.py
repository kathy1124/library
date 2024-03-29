from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    quantity = models.IntegerField()
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    picture = models.CharField(max_length=500)
    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

from django.contrib.auth.models import User

class Borrow_book(models.Model):
    readerID = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.ForeignKey(Post, on_delete=models.PROTECT)
    borrow_date = models.DateTimeField()  #借書時間
    due_date = models.DateTimeField()     #到期日
    returned = models.BooleanField(default=False)
    actual_return_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ("readerID", "title", "borrow_date")
