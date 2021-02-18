from django.contrib import admin
from blog.models import Blog, Tags, Comment


class AdminBlog(admin.ModelAdmin):
    class Meta:
        fields = ['title', 'user']


class AdminTags(admin.ModelAdmin):
    class Meta:
        fields = ['name', 'id']


admin.site.register(Blog, AdminBlog)
admin.site.register(Tags, AdminTags)
admin.site.register(Comment)