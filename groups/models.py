from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse
import misaka

User = get_user_model()

from django import template
register = template.Library() # it is used to register own template tags 


# Create your models here.
class Group(models.model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self .name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(description_html)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

class GroupMembers(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_groups')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='memberships')
    
    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('groups', 'users')