from django.contrib import admin

# Register your models here.
from blog.models import Blog


# Register Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)
    search_fields = ('title',)