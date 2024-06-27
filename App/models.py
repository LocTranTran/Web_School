from django.db import models # type: ignore

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.CharField(max_length=100 , null = True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    