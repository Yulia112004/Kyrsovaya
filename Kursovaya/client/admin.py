from django.contrib import admin

# Register your models here.
from client.models import Client


# Register Blog

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment',)
    search_fields = ('name',)