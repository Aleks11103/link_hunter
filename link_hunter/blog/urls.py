from django.urls import path
from blog import views as blog
from django.shortcuts import redirect


urlpatterns = [
    path('all/<int:page_id>/', blog.records, name='blog_records'),
    path('single/<int:blog_id>/', blog.record, name='blog_record'),
    path('', lambda x: redirect('all/1')),
]
