(function(){
     let standardUpload =document.getElementById('standard-upload')
      let dropzone=document.getElementById('drop-zone')
      let token=document.getElementsByName("csrfmiddlewaretoken")[0].value;
      let progressbar=document.getElementById('bar-fill');
      let progressText=document.getElementById('bar-text');
      let uploadfinished=document.getElementById('upload-finish');
      let uploadinfo=document.getElementById('upload-info')
      let filefield=document.getElementById('video_id')
      let uploadarea=document.getElementById('upload-area')
        startUpload=function(file){
            app.uploader({
                file:file,
                token:token,
                progressbar:progressbar,
                progressText:progressText,


                completed:function(data){
                    var uploadedElement;
                    var uploadedVideo;
                    var videosource;
                    uploadedElement=document.createElement('div')
                    uploadedElement.className='upload-display';
                    uploadedVideo=document.createElement('video')
                    uploadedVideo.controls=true
                    videosource=document.createElement('source');
                    videosource.src=data.video_path;
                    videosource.type='video/mp4';
                    
                    uploadedVideo.appendChild(videosource);
                    uploadedElement.appendChild(uploadedVideo);
  
                    uploadfinished.appendChild(uploadedElement)
                    uploadfinished.className='upload-completed';

                    uploadarea.className='hidden';
                    uploadinfo.className='video-info'
                    filefield.value=data.video_id

                            
                },
                error:function(){
                    console.log('upload was not successful')
                }

            })
        }

      standardUpload.addEventListener('click', function(e){
          e.preventDefault()
          let filetoUpload=document.getElementById('file-upload').files
          startUpload(filetoUpload)

      })
      dropzone.ondrop=function(e){
          e.preventDefault()
           startUpload(e.dataTransfer.files)
      }

      dropzone.ondragover=function(){
          this.className="upload-drop drop"
          return false
      }
      dropzone.ondragleave=function(){
          this.className="upload-drop"
          return false

      }



}())