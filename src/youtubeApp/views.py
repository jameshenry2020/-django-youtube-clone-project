from django.shortcuts import render,redirect,get_object_or_404
from .forms import ChannelForm,EditChannelForm
from .models import Channel,VideoFiles,VideoDetail
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def create_channel(request):
    user=request.user
    if request.method =="POST":
        form=ChannelForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            category=form.cleaned_data.get('category')
            Channel.objects.create(name=name, user=user,slug=user.username, category=category)
            return redirect("mychannel", slug=user.username)

    else:
        form=ChannelForm()
        context={
            "channel_form":form
        }
    return render(request, "channel/create.html", context)

def channel(request, slug):
    mychannel=Channel.objects.get(slug=slug)
    channel_videos=VideoFiles.objects.filter(channel=mychannel)
    context={
        "channel":mychannel,
        "my_videos":channel_videos
    }

    return render(request, "channel/channel_home.html", context)

def index(request):
    allvideos=VideoFiles.objects.all()
    allvideos=allvideos.filter(videodetail__visibility=True)
    context={
        "videos":allvideos
    }
    return render(request, "videos/index.html", context)

def video_watch_view(request, video_id):
    video=get_object_or_404(VideoFiles, id=video_id)
    context={
        "my_video":video
    }

    return render(request, "videos/watch.html", context)


def edit_channel(request, slug):
    channel=Channel.objects.get(slug=slug)
    if request.method =="POST":
        form=EditChannelForm(request.POST, request.FILES, instance=channel)
        if form.is_valid():
            form.save()
            return redirect("mychannel", slug=request.user.username)           
    else:
        form=EditChannelForm(instance=channel)
        context={
            "edit_form":form
        }

    return render(request, "channel/edit_channel.html", context)

@login_required
def upload_view(request):
    return render(request, "channel/fileupload.html")


def upload_processing(request):
    channel=Channel.objects.get(slug=request.user.username)
    if channel is not None:
        if request.method =="POST":
            file=request.FILES['file']
            upload=VideoFiles.objects.create(video=file, channel=channel)
            data={
                'video_id':upload.id,
                "video_path":upload.video.url
            }
            return JsonResponse(data, safe=False)
        return JsonResponse({'error':'an error ocurred'})
    else:
       # messages.info( sorry you dont have channel please create one)
        return redirect("file-upload")


def video_info_process(request):
    if request.method == "POST":
        file_id=request.POST['videofile']
        title=request.POST['title']
        desc=request.POST['description']
        visibility=request.POST['visibility']
        thumbnail=request.FILES['thumbnail']

        video=get_object_or_404(VideoFiles, id=file_id)
        VideoDetail.objects.create(videofile=video,title=title, description=desc, visibility=visibility, thumbnail=thumbnail)
         #message video uploaded successful
        return redirect('mychannel', slug=request.user.username)
    return redirect('file-upload')
