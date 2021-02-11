from django.contrib import admin
from .models import *
from .forms import *

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    search_fields = ["name", "slug", "description", "created", "updated"]
    list_display = ["name", "slug", "description", "created", "updated"]
    readonly_fields = [ 'created', 'updated']

# Register your models here.
admin.site.register(Category, CategoryAdmin)