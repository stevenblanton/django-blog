from django.contrib import admin
from blogging.models import Post, Category


class PostCategory(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostCategory,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)