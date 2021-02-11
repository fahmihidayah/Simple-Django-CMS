from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

from .mixins import ContentMixin, PageMixin

from category.models import Category
from content.models import Content

# Create your views here.


class HomeView(TemplateView, PageMixin, ContentMixin):

    template_name = 'front_end/home.html'

    def get_title_page(self):
        return 'Home'


class ContentDetailView(DetailView, PageMixin):
    model = Content
    template_name = 'front_end/content_detail.html'

    def get_title_page(self):
        return self.object.title


class SearchContentView(TemplateView, PageMixin, ContentMixin):

    template_name = 'front_end/search_result.html'

    def get_title_page(self):
        return "Hasil pencarian"
