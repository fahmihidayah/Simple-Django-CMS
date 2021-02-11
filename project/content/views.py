from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import *
from .tables import *
from django_tables2 import SingleTableView
from django.urls import reverse
# Create your views here.

class ContentListView(SingleTableView):
    model = Content
    paginate_by = 10
    table_class = ContentTable

    def get_queryset(self):
        return Content.objects.all()


class ContentCreateView(CreateView):
    model = Content
    form_class = ContentForm


class ContentDetailView(DetailView):
    model = Content
    template_name = "content/content_detail.html"


class ContentUpdateView(UpdateView):
    model = Content
    form_class = ContentForm


class ContentDeleteView(DeleteView):
    model = Content

    def get_success_url(self):
        return reverse('content_list')