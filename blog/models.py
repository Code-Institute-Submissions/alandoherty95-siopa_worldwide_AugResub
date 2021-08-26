from django.db import models


# BLOGPOST FORM MODEL
class BlogPost(models.Model):
    class Meta:
        verbose_name = 'Blog Post'

    title = models.CharField(max_length=254, null=False, blank=False)
    slug = models.SlugField(max_length=254, unique=True)
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    original_url = models.URLField(max_length=1024, blank=True, null=True)
    date_created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title
