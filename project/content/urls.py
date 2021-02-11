from django.urls import path
from .views import *

urlpatterns = [
    path('content', ContentListView.as_view(), name='content_list'),
    path('content/create', ContentCreateView.as_view(), name='content_create'),
    path('content/<slug:slug>', ContentDetailView.as_view(), name='content_detail'),
    path('content/update/<slug:slug>', ContentUpdateView.as_view(), name='content_update'),
    path('content/delete/<slug:slug>', ContentDeleteView.as_view(), name='content_delete'),
]