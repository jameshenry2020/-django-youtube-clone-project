from django.contrib import admin
from .models import Channel, Category,VideoFiles,VideoDetail, ViewCount, VideoComment

# Register your models here.
admin.site.register(Category)
admin.site.register(Channel)
admin.site.register(VideoFiles)
admin.site.register(VideoDetail)
admin.site.register(ViewCount)
admin.site.register(VideoComment)
