from django.contrib import admin
from .models import *
from .forms import *
from django_summernote.admin import SummernoteModelAdmin


class ContentAdmin(SummernoteModelAdmin):
    form = ContentForm
    search_fields = ["title", "slug", "text", "created", "updated"]
    list_display = ["title", "slug", 'status', "created", "updated"]
    readonly_fields = [ 'created', 'updated']

    summernote_fields = '__all__'

    def get_form(self, request, obj=None, change=False, **kwargs):
        form: ContentForm = super(ContentAdmin, self).get_form(request=request, obj=obj, change=change, **kwargs)
        form.current_user = request.user
        return form

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ContentAdmin, self).save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Content, ContentAdmin)