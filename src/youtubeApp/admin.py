from django.contrib import admin
from .models import Channel, Category,VideoFiles,VideoDetail

# Register your models here.
admin.site.register(Category)
admin.site.register(Channel)
admin.site.register(VideoFiles)
admin.site.register(VideoDetail)
