from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Blog, Tags


# def records(request, page_id):
#     count = 6
#     start = count * page_id - count
#     context = {'records': Blog.objects.all()[start:start+count]}
#     return render(request, 'blogs.html', context)


# def filtred_records(request, tag_name):
#     count = 6
#     start = count * 1 - count
#     context = {'records': Blog.objects.filter(tags__name=tag_name)[start:start+count]}
#     return render(request, 'blogs.html', context)


# def record(request, blog_id):
#     context = {'record': Blog.objects.get(id=blog_id)}
#     return render(request, 'blog.html', context)


class AllBlogs(ListView):
    model = Blog
    template_name = 'blogs.html'
    paginate_by = 4

    def get_queryset(self):
        if self.request.GET.get('tag'):
            return self.model.objects.filter(tags__name=self.request.GET.get('tag'))
        return super().get_queryset()

# class FilterBlog(ListView):
#     model = Blog
#     template_name = 'blogs.html'
#     paginate_by = 3

#     def get_queryset(self):
#         return self.model.objects.filter(tags__name=self.request.GET.get('tag'))

class OneBlog(DetailView):
    model = Blog
    template_name = 'blog.html'