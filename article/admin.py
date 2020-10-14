from django.contrib import admin

#2 Register your models here.
from .models import Article, Comment

admin.site.register(Comment)

#admin.site.register(Article)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title", "author", "created_date"]
    list_display_links =["title", "author"]
    search_fields=["title"]
    list_filter = ["created_date", "title"]

    class Meta:
        model = Article

