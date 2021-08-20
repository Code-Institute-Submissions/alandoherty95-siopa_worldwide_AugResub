from django.db import models


class BlogPost(models.Model):
    class Meta:
        verbose_name = 'Blog Post'

    title = models.CharField(max_length=254, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
