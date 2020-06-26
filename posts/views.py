from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404

from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class PostListView(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'group')

class UserPostView(generic.ListView):
    model = models.post
    template_name = 'post/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetailView(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        querryset = super().get_queryset()
        return querryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePostView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ['message', 'group']
    model = models.Post

    def form_valid(self, form):
        form.instance.user = self.request
        return super().form_valid(form)

class DeletePostView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('post:all')

    def get_querryset(self):
        querry = super().get_queryset
        return querry.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        message.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)