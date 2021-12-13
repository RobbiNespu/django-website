from django.contrib import admin
from .models import Post, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    radio_fields = {"source": admin.HORIZONTAL}
    list_display = ('title', 'slug', 'status', 'creation_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
