from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import *
from .tables import *
from django_tables2 import SingleTableView
from django.urls import reverse
# Create your views here.

class CategoryListView(SingleTableView):
    model = Category
    paginate_by = 10
    table_class = CategoryTable

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category/category_detail.html"


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm


class CategoryDeleteView(DeleteView):
    model = Category

    def get_success_url(self):
        return reverse('category_list')