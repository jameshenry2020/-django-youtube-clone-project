from django.urls import path
from .views import ( create_channel,
                    channel,
                    edit_channel,
                    upload_view,
                    upload_processing,
                    video_info_process,
                    index,
                    video_watch_view,
                    liked_video,
                    dislike_video,
                    subscriber_view,
                    video_comment,
                    dashboard,
                    update_video,
                    delete_video
                    
                   )


urlpatterns=[
    path('', index, name="home"),
    path("watch/?v=<uuid:video_id>", video_watch_view, name="video_watch"),
    path("channel/create/", create_channel, name="create"),
    path("channel/<slug>/", channel, name="mychannel"),
    path("channel/dashboard/<slug>/", dashboard, name="channel-dashboard"),
    path("like/<uuid:id>/", liked_video, name="like-video"),
    path("channel/edit_video/<uuid:id>", update_video, name="update-video"),
    path("channel/delete_video/<uuid:id>", delete_video, name="delete-video"),
    path("dislike/<uuid:id>/", dislike_video, name="dislike-video"),
    path("update_channel/<slug>/", edit_channel, name="update-channel"),
    path("upload/", upload_view, name="file-upload"),
    path("uploading/", upload_processing, name="processing"),
    path("video_detail/", video_info_process, name="video-data"),
    path("subscribe/", subscriber_view, name="subscriber"),
    path("user_comment/<uuid:video_id>", video_comment, name="comment"),
]