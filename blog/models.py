from django.db import models


class BlogPost(models.Model):
    class Meta:
        verbose_name = 'Blog Post'

    title = models.CharField(max_length=254, blank=False, null=False)
    slug = models.SlugField(max_length=254, unique=True)
    body = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title