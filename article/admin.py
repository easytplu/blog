from curses import tigetflag
from re import search
from turtle import title
from django.contrib import admin
from .models import Article,Comment
# Register your models here.
admin.site.register(Comment)
#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date","content"]
    
    list_display_links = ["title","created_date"] 
    
    search_fields = ["title"]
    
    list_filter = ["created_date"]
    #list_filter = ["title"]
    #list_filter = ["content"]
    class Meta:
        model = Article