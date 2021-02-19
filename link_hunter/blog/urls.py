from django.urls import path
from blog import views as blog
from django.shortcuts import redirect


urlpatterns = [
    path('<int:pk>/', blog.OneBlog.as_view(), name='blog_record'),
    path('all/', blog.AllBlogs.as_view(), name='blog_records'),
    # path('all/<int:page_id>/', blog.records, name='blog_records_with_pagination'),
    # path('single/<int:blog_id>/', blog.record, name='blog_record'),
    # path('filtred/', blog.FilterBlog, name='filtred_blog_records'),
    # path('', lambda x: redirect('all/1')),
]
