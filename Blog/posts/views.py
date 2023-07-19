from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

def homePage(request):
    return render(request, 'posts/home.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/index.html'



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

# class ListCreate(CreateView):
#     model = Post
#
#     def get_context_data(self):
#         context = super(ListCreate, self).get_context_data()
#         context["title"] = "Add a new list"
#         return context
#
# class ListDelete(DeleteView):
#     model = Post
#     success_url = reverse_lazy("index")

