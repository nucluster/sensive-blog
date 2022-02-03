from django.contrib import admin
from blog.models import Post, Tag, Comment


# admin.site.register(Tag)
# admin.site.register(Comment)
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes', 'author', 'tags',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author',)