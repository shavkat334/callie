from django.contrib import admin

from .models import Author, Category, Comment, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
