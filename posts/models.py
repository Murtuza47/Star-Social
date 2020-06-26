from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka
from groups.models import Group

from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(Users,related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True) 
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message = misaka.html(message_html)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username':self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_date']
        unique_together = ['message','users']