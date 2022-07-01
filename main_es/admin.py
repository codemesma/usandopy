from django.contrib import admin
from .models import Tutorial, Categoria, Tipo, Sobre, Author


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')


class TipoAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'category', 'status')


admin.site.register(Categoria, CategoryAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Tutorial, PostAdmin)
admin.site.register(Sobre)
admin.site.register(Author)
