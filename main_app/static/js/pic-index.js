const likeIcon = document.querySelector('#icon');

let clicked = false; 

function changeColor(){
 
  if(!clicked){
    clicked = true; 
    likeIcon.innerHTML = '<i class="fas fa-heart"></i>';
    likeIcon.style.color = 'red';
  }
  else {
    clicked = false;
    likeIcon.innerHTML = '<i class="far fa-heart"></i>';
    likeIcon.style.color = 'red';
  }
}


