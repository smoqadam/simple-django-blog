from django.db import models


# Create your models here.

class Blog(models.Model):
    POST_TYPE = (
        ('post', 'Post'),
        ('page', 'Page')
    )
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    type = models.CharField(max_length=10, choices=POST_TYPE, default='post')
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def __str__(self):
        return self.slug


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.slug
