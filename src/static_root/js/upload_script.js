(function(){
     let standardUpload =document.getElementById('standard-upload')
      let dropzone=document.getElementById('drop-zone')
      let token=document.getElementsByName("csrfmiddlewaretoken")[0].value;
      let progressbar=document.getElementById('bar-fill');
      let progressText=document.getElementById('bar-text');
      let finished=document.getElementById('upload-finish')
        startUpload=function(file){
            app.uploader({
                file:file,
                token:token,
                progressbar:progressbar,
                progressText:progressText,


                completed:function(data){
                    var uploadedElement, uploadedVideo, videosource;
                     uploadedElement=document.createElement('div')
                     uploadedElement.className='upload-display'
                     uploadedVideo=document.createElement('video')
                     uploadedVideo.controls=true
                     uploadedVideo.width='320'
                     uploadedVideo.height='240'
                     videosource=document.createElement('source')
                     videosource.src=data.video_path
                     videosource.type="video/mp4"
                     uploadedVideo.appendChild(videosource)
                     uploadedElement.appendChild(uploadedVideo)
                     finished.appendChild(uploadedElement)
                     finished.className="upload-completed"
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