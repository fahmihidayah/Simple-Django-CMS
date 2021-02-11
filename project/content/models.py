from django.db import models

from django_extensions.db import fields

from category.models import Category
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from enum import Enum
# Create your models here.
UserModel = get_user_model()

CONTENT_STATUS = [
    ('dr', 'draft'),
    ('sh', 'show'),
    ('ar', 'archive'),
]


class ContentQuerySet(models.QuerySet):

    def by_keyword(self, keyword):
        return self.filter(title__icontains=keyword).filter(title__icontains=keyword)

    def by_category(self, category):
        return self.filter(categories__name__icontains=category)

    def show_content(self):
        return self.filter(status='sh')


class ShowContentManager(models.Manager):

    def get_queryset(self):
        return ContentQuerySet(self.model, using=self._db)

    def get_show_content(self):
        return self.get_queryset().show_content()


class Content(models.Model):

    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, )

    image = models.ImageField(upload_to='content/uploads/%Y-%m-%d/', default='')

    title = models.CharField(max_length=100, default='', null=False)

    slug = fields.AutoSlugField(populate_from='title')

    text = models.TextField(max_length=255, default='', null=False)

    categories = models.ManyToManyField(to=Category)

    show_objects = ShowContentManager()

    status = models.CharField(
        max_length=2,
        choices=CONTENT_STATUS,
        default='sh'
    )

    created = models.DateTimeField(auto_now=True, editable=False)

    updated = models.DateTimeField(auto_now_add=True, editable=False)




    def get_absolute_url(self):
        return reverse('content_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('content_update', args=(self.slug,))

    def get_delete_url(self):
        return reverse('content_delete', args=(self.slug,))

    def get_list_url(self):
        return reverse('content_list')

    def get_create_url(self):
        return reverse('content_create')