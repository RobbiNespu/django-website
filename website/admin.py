from django.contrib import admin
from .models import Post, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    radio_fields = {"source": admin.HORIZONTAL}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
