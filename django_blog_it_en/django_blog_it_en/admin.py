from django.contrib import admin
from .models import Post, Category, Tags, Author, Equipa, Canal, Feedback


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'is_active')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'category', 'status')


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'email',)


class EquipaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'email', )


class CanalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'web')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


admin.site.register(Feedback, FeedbackAdmin)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tags, TagsAdmin)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Equipa, EquipaAdmin)
admin.site.register(Canal, CanalAdmin)
