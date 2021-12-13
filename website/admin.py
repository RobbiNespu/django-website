from django.contrib import admin
from .models import Post, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    radio_fields = {"source": admin.HORIZONTAL}
    list_display = ('title', 'slug', 'status', 'creation_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
