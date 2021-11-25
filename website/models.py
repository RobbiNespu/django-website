from ckeditor_uploader.fields import RichTextUploadingField
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

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    kind = models.ForeignKey(IndiewebKind, on_delete=models.CASCADE)
    source = models.ForeignKey(IndiewebSource, on_delete=models.CASCADE,null=True)
    webMention = models.URLField(verbose_name="Webmention target", max_length=200, default="")
    # intro = models.TextField(max_length=200) // for TLDR or meta decription but let comment out for now
    body = RichTextUploadingField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-creation_date']
        get_latest_by = 'creation_date'
        indexes = [
            models.Index(fields=['-creation_date'])
        ]

