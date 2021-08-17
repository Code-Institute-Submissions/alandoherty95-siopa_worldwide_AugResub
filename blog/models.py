from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):

    title = models.CharField(max_length=120,
                             null=True, blank=False)
    subtitle = models.CharField(max_length=180,
                                null=True, blank=False)
    body = models.TextField()
    slug = models.SlugField(unique=True,
                            max_length=250, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):

        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while BlogPost.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the slug
        if it hasn't doesn't exist yet.
        """

        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
