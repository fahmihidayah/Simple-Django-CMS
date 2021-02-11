from django_tables2 import Table, TemplateColumn
from .models import Content

class ContentTable(Table):

    detail = TemplateColumn(template_name='table/detail.html')

    edit = TemplateColumn(template_name='table/edit.html')

    delete = TemplateColumn(template_name='table/delete.html')

    class Meta:
        model = Content
        fields = ["title", "slug", "created", "updated"]
        template_name = 'django_tables2/bootstrap.html'
