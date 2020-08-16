from django.shortcuts import render
from django.views import generic
from .models import posts,tags

class PostList(generic.ListView):
    queryset= posts.objects.order_by('-created_on')
    template_name='index.html'

class PostDetail(generic.DetailView):
    model=posts
    template_name='post_detail.html'
class contact(generic.ListView):
    queryset= posts.objects.order_by('-created_on')
    template_name='contacts.html'
class home(generic.ListView):
    queryset= posts.objects.order_by('-created_on')
    template_name='home.html'
class taglist(generic.ListView):
     model=posts
     template_name='tags.html'
     def get_queryset(self,**kwargs):
          pk = self.kwargs['pk']
          return posts.objects.filter(tags=pk)
# Create your views here.
