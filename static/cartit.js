let alldivs = document.getElementById('carite');
let nav = document.getElementById('navbar');



window.addEventListener('scroll',()=>{
    if(alldivs.getBoundingClientRect().top<0){
        nav.style.cssText = 'box-shadow:0px 0px 25px black; background-color:white';
    }
    else{
        nav.style.backgroundColor = '#FFCE32';
        nav.style.cssText = 'box-shadow:none';
    }
})

let cartanchor = document.getElementById('cartanchor');

if(window.location.href == 'https://jayakara.pythonanywhere.com/APP/cart/'){
    cartanchor.style.color = 'blue';
}
else{
    cartanchor.style.color = 'black';
}