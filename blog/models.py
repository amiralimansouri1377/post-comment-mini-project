from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    post_text = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail-post", args=[self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    email = models.CharField(max_length=100)
