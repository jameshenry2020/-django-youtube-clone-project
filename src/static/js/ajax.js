$(document).ready(function(){

    //like ajax call
    $('.like-form').submit(function(e){
        e.preventDefault();
         const video_id=$('.like-btn').val();
         const token=$('input[name=csrfmiddlewaretoken]').val();
         const url=$(this).attr('action') 
       $.ajax({
           method:"POST",
           url:url,
           headers:{'X-CSRFToken': token},
           data:{
               'video_id':video_id
           },
           success:function(response){
            if(response.liked===true){
                $('.like-icon').addClass('text-blue-700')
              }else{
                $('.like-icon').removeClass('text-blue-700')
              }
            
               like=$('#like-count').text(response.likes_count)
               parseInt(like)
           },
           error:function(response){
            console.log("Failed ", response)
           }
       })
    })


    //dislike ajax call

    $('.dislike-form').submit(function(e){
        e.preventDefault()
       const video_id=$(".dislike-btn").val()
       const token=$('input[name=csrfmiddlewaretoken]').val() 
       const url =$(this).attr('action') 
          $.ajax({
               method:"POST",
               url:url,
               headers:{"X-CSRFToken": token},
               data:{
                   'video_id':video_id
               },
               success:function(response){
                   console.log(response)
                   if(response.disliked ===true){
                       $(".dislike-icon").addClass("text-blue-700")
                   }else{
                       $(".dislike-icon").removeClass("text-blue-700")
                   }
               
                   dislikes=$("#dislike-count").text(response.dislike_count)
                   parseInt(dislikes)
                   
               },
               error:function(response){
                   console.log('failed', response)
               }
           }) 
   
   })


   //subcriber ajax call
   $('.Subcriber_form').submit(function(e){
       e.preventDefault()
       const channel_id=$('.sub-btn').val()
       const token=$('input[name=csrfmiddlewaretoken').val() 
       const url =$(this).attr('action')
       
       $.ajax({
        method:"POST",
        url:url,
        headers:{"X-CSRFToken": token},
        data:{
            'channel_id':channel_id
        },
        success:function(response){
            if(response.Subscribed==true){
                $('.sub-btn').removeClass("bg-red-700")
                 $('.sub-btn').addClass("bg-gray-600")
                 
             }else{
                $('.sub-btn').removeClass("bg-gray-600")
                $('.sub-btn').addClass("bg-red-700")

             }
             $('.sub-count').text(response.num_subscribers)
       
           console.log(response)
        },
        error:function(response){
           console.log("failed ", response)
        }
    })

 
   })
   
})