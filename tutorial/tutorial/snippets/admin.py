from django.contrib import admin

# Register your models here.

from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'code')


    list_per_page = 10

admin.site.register(Snippet, SnippetAdmin)
