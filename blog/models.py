from django.db import models


class BlogPost(models.Model):
    class Meta:
        verbose_name = 'Blog Post'

    title = models.CharField(max_length=254, blank=False, null=False)
    slug = models.SlugField(max_length=254, unique=True)
    intro = models.TextField(blank=False, null=False)
    body = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
