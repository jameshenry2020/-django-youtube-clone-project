from django.urls import path
from .views import ( create_channel,
                    channel,
                    edit_channel,
                    upload_view,
                    upload_processing,
                    video_info_process,
                    index,
                   )


urlpatterns=[
    path('', index, name="home"),
    path("channel/create/",create_channel, name="create-channel"),
    path("channel/<slug>/", channel, name="mychannel"),
    path("update_channel/<slug>/", edit_channel, name="update-channel"),
    path("upload/", upload_view, name="file-upload"),
     path("uploading/", upload_processing, name="processing"),
    path("video_detail/", video_info_process, name="video-data")

]