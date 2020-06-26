from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, RedirectView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.contrib import messages
from .models import Group, GroupMembers
# Create your views here.

class CreateGroupView(LoginRequiedMixin,CreateView):
    model = Group
    fields = ['name', 'description']

class SingleGroup(DetailView):
    model = Group

class ListGroup(ListView):
    model = Group

    
class LeveGroupView(LoginRequiedMixin, RedirectView ):
    def get_redirect_url(self,**args,**kwargs):
        return reverse('groups:single' kwargs={'slug':slef.kwargs.get('slug')})

    def get(self,*args,**kwargs):
        try:
            membership = GroupMembers.objects.filter(
                user = self.request.user
                group__slug = self.kwargs.get('slug')   
            ).get()
        except:
            messages.warning(self.request,'You are not in this group')
        else:
            membership.delet()
            messages.success(self.request,'You have left the group')
        return super().get(*args,**kwargs)

class JoinGroupView(LoginRequiedMixin, RedirectView ):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single' kwargs={'slug':slef.kwargs.get('slug')})

    def get(self,*args<**kwargs):
        group =get_object_or_404(Group,slug=self.kwargs.slug)

        try:
            GroupMembers.objects.create(user=self, group=group)
        except:
            messages.warning(self.request,'Warning already a member')
        else:
            messages.success(self.request, "You are now a member")
        return super().get(*args,**kwargs)