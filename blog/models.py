from django.db import models
from django.urls import reverse


class BlogDB(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    ) # on_delte is a must for foregin key
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogdetail', kwargs={'pk': self.pk})