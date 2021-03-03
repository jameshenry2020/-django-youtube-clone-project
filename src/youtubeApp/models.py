import uuid
from django.db import models
from django.shortcuts import reverse
from django.conf import settings

def channel_directory_path(instance, filename):
    return "video_files/channel_{0}/{1}".format(instance.channel.id, filename)

User=settings.AUTH_USER_MODEL
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Channel(models.Model):
    name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    channel_art=models.ImageField(upload_to="channel/", default='default_art.jpg')
    channel_icon=models.ImageField(upload_to='profile/', default='default_icon.png')
    slug=models.SlugField()
    description=models.TextField(blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    subcribers=models.ManyToManyField(User, related_name="subscribers")
    def __str__(self):
        return self.name

    def num_subcribers(self):
        return self.subcribers.count()

class VideoFiles(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video=models.FileField(upload_to=channel_directory_path)
    channel=models.ForeignKey(Channel, on_delete=models.CASCADE)
    uploaded=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User, related_name="video_loved")
    dislikes=models.ManyToManyField(User, related_name="video_disliked")

    def __str__(self):
        return f"video_file_{self.id}"

    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('video_watch', args=[str(self.id)])
    
    def num_likes(self):
        return self.likes.count()

    def num_dislikes(self):
        return self.dislikes.count()

class VideoDetail(models.Model):
    videofile=models.OneToOneField(VideoFiles, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    visibility=models.BooleanField(choices=((False, "private"),(True, "public")))
    thumbnail=models.ImageField(upload_to="thumbnail/")

    def __str__(self):
        return self.title
class ViewCount(models.Model):
    video=models.ForeignKey(VideoFiles, related_name="view_count", on_delete=models.CASCADE)
    ip_address=models.CharField(max_length=50)
    session=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ip_address}"

class VideoComment(models.Model):
    video=models.ForeignKey(VideoFiles, related_name="comments", on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} comment"