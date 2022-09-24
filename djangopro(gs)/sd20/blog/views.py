from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# 126
from django.views.generic import ListView, DetailView
from django.http import Http404
# Create your views here.

# Pagination with Function Based View 125
def post_list(request):
    all_posts = Post.objects.all().order_by('id')
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'blog/home.html', {'page_obj':page_obj})

###################################################################
# Pagination with Class Based View 126
class PostListView(ListView):
    model = Post
    template_name='blog/home2.html'
    ordering = ['id']
    paginate_by = 3
    # paginate_orphans = 1

    # for 404 error if page not exist both same
    def get_context_data(self, **kwargs):
        try:
            return super(PostListView, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView, self).get_context_data(**kwargs)

    # for 404 error if page not exist both same
    # def paginate_queryset(self, queryset, page_size):
    #     try:
    #         return super(PostListView, self).paginate_queryset(queryset, page_size)
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         return super(PostListView, self).paginate_queryset(queryset, page_size)    

class PostDetailView(DetailView):
    model = Post
    template_name='blog/postdetail.html'