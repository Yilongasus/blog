from django.contrib import admin

from article.models import Article, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'content']
    list_display_links = ['article']
    list_filter = ['article', 'content','pubDateTime']
    search_fields = ['content']
    list_editable = ['content']
 
    class Meta:
        model = Comment


admin.site.register(Article)
admin.site.register(Comment, CommentAdmin)
