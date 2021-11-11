from django.db import models


# Create your models here.
class IndiewebKind(models.Model):
    kind = models.CharField(max_length=14)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.kind


class IndiewebSource(models.Model):
    source = models.CharField(max_length=14, default='website')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.source


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    kind = models.ForeignKey(IndiewebKind, on_delete=models.CASCADE)
    source = models.ForeignKey(IndiewebSource, on_delete=models.CASCADE,null=True)
    intro = models.TextField(max_length=150)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
