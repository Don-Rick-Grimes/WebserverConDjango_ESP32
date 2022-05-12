from django.contrib import admin
from .models import Categoria,Post

# Register your models here.
class CategoriaAndmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAndmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Categoria, CategoriaAndmin)
admin.site.register(Post, PostAndmin)
