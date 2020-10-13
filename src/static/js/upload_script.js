(function(){
     let standardUpload =document.getElementById('standard-upload')
      let dropzone=document.getElementById('drop-zone')
        startUpload=function(file){
            console.log(file)
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