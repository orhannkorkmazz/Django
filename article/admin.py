from django.contrib import admin
from . models import Article,Comment,UserProfile
from django.contrib import admin




# Register your models here.
admin.site.register(Comment)#Comment modelini form oluşturmadan kaydettim
admin.site.register(UserProfile)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'author', 'created_date')
    list_display_links=['title']
    list_filter = ('created_date', 'author')
    search_fields = ('title', 'content')
    class Meta:
        model=Article

