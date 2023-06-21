from django.db import models

# Create your models here.
class Post(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    author = models.CharField(max_length=100)
    post_text = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    email = models.CharField(max_length=100)
