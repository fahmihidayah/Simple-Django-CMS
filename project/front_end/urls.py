from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('content-detail/<slug:slug>', ContentDetailView.as_view(), name='content_detail_view'),
    path('search', SearchContentView.as_view(), name='search_content'),
]