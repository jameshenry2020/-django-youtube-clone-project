video management system like youtube ( youtube clone)

 project todo's
 
 setup development env
 authentication django allauth
 register create channel
 edit channel
 upload videos
 watch uploaded videos
 like or dislike the video
 comment on the video
 get the view count(anonymous | register)
 edit video
 delete video

  model structure
 User

 Category
    name (blog education, entertainment, technology)

 Channel
     name
     user
     channel art
     channel icon
     description
     category

 Video
     id uuid
     video
     channel 
     uploaded
    
 VideoDetail
     videofile
     title
     description
     visibility
     thumbnail
