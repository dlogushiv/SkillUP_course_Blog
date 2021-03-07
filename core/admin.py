from django.contrib import admin

# Register your models here.

from .models import Post, Comment


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     search_fields = ('text',)
#     list_filter = ('author', 'post',)
#     list_display = ('text', 'author', 'post',)  # create columns of ('', '') which can sort
# class CommentAdmin can be deleted/hide if present class CommentInline
# because all comment will visible after each post

# class <name>Inline used for adding some objects to another class,
# e.g. for post, comments will shows after post

class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body',)  # create search field with searching by ('', '')
    list_filter = ('author',)  # 'title',)  # create filter side bar with filtering by ('', '')

    inlines = (CommentInline,)      # iterable object, tuple or list of inline classes

# admin.site.register(Post)
