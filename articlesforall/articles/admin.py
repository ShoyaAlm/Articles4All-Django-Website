from django.contrib import admin
from .models import Author, Article, Topic

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Topic)