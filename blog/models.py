from django.db import models


class BlogPost(models.Model):
    class Meta:
        verbose_name = 'Blog Post'

    title = models.CharField(max_length=254, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title
