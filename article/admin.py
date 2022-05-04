from django.contrib import admin
from .models import Article,Comment
# Register your models here.
@admin.register(Article) #admin paneli görselleştirme
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta: #article admin ile article ı bağliyoruz
        model = Article
admin.site.register(Comment)
