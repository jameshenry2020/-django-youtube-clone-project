var create_btn=document.getElementById('open');

var modal =document.getElementById('modal');
var close_btn=document.getElementById('close_btn');
var closeBtn=document.getElementById('close');

create_btn.addEventListener('click', openModal);
close_btn.addEventListener('click', closeModal);
window.addEventListener('click', clickOutside);
closeBtn.addEventListener('click', closeModal)

function openModal(){
    modal.style.display='block'
}
function closeModal(){
    modal.style.display='none'
}
function clickOutside(e){
    if(e.target==modal){
       modal.style.display='none' 
    }
    
}


// channel tab script 


