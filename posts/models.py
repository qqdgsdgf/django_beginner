from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        """control the name of new section added from admin page"""
        return self.text[:50]

