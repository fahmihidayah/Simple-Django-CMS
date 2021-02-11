from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from category.models import Category
from content.models import Content


class MenuMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        return context


class CategoryMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(CategoryMixin, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ContentMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(ContentMixin, self).get_context_data(**kwargs)
        keyword = self.request.GET.get('keyword', '')
        category = self.request.GET.get('category', '')
        context['keyword'] = keyword
        context['category_name'] = category
        context['contents'] = Content.show_objects.get_show_content().by_keyword(keyword).by_category(category)

        return context


class TitleMixin(ContextMixin):

    def get_title_page(self):
        return 'Unknown'

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.get_title_page()
        return context


class PageMixin(TitleMixin, CategoryMixin):
    pass
