from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published', 'slug', 'user')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title', 'text', 'slug')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
