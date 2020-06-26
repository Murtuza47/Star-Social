from django.contrib import admin
from . import models
# Register your models here.
class GroupMemeberInline(admin.TabularInline):
    model = models.GroupMemeber

admin.site.register(models.Group)