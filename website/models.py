from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    INDIEWEB_KINDS = (
        ("article", "article"),
        ("status", "status"),
        ("in-reply-to", "in-reply-to"),
        ("rsvp", "rsvp"),
        ("like-of", "like-of"),
        ("bookmark", "bookmark"),
        ("checkin", "checkin"),
        ("repost-of", "repost-of"),
        ("photo", "photo"),
        ("sport", "sport"),
    )
    kind = models.CharField(
        max_length=13,
        choices=INDIEWEB_KINDS,
        default="article",
    )

    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
