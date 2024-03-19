let th = document.getElementById('Eheading');
let nav = document.getElementById('navbar');
let bd = document.getElementsByTagName('body')[0];


// console.log(nav);
// th.addEventListener('click',()=>{
    // th.style.color = 'black'
// })




window.addEventListener('scroll',()=>{
    console.log(th.getBoundingClientRect());
    if(th.getBoundingClientRect().top < 20){
        nav.style.cssText = 'box-shadow:0px 0px 25px black; background-color:white';
        // bd.style.backgroundColor = '#FFCE32';
    }
    else{
        nav.style.backgroundColor = '#FFCE32';
        nav.style.cssText = 'box-shadow:none';
        // bd.style.backgroundColor = 'white';
    }
})