from django.contrib import admin
from apps.blog.models import Blog, Category, Comment


class CommentAdmin(admin.StackedInline):
    model = Comment

@admin.register(Blog)
class BostAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin]
    list_display = ('title', 'published')
    class Meta:
        model = Blog


admin.site.register(Category)

