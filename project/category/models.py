from django.db import models
from django_extensions.db import fields
# Create your models here.
from django.urls import reverse

# DJENERATE-IGNORE

class Category(models.Model):

    name = models.CharField(max_length=50, default='', null=False)

    slug = fields.AutoSlugField(populate_from='name')

    description = models.CharField(max_length=100, default='', null=False)

    created = models.DateTimeField(auto_now=True, editable=False)

    updated = models.DateTimeField(auto_now_add=True, editable=False)


    def get_absolute_url(self):
        return reverse('category_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('category_update', args=(self.slug,))

    def get_delete_url(self):
        return reverse('category_delete', args=(self.slug,))

    def get_list_url(self):
        return reverse('category_list')

    def get_create_url(self):
        return reverse('category_create')

    def __str__(self):
        return self.name