let customer = document.getElementById('customer');
let admin = document.getElementById('admin');

let nav = document.getElementById('navbar');



window.addEventListener('scroll',()=>{
    if(admin.getBoundingClientRect().top<150){
        nav.style.cssText = 'box-shadow:0px 0px 25px black; background-color:white';
    }
    else{
        nav.style.backgroundColor = '#FFCE32';
        nav.style.cssText = 'box-shadow:none';
    }
})

// =================================================================================


let useranchorlink = document.getElementById('useranchorlink');

    if(location.href == 'https://jayakara.pythonanywhere.com/APP/user/' ){
        useranchorlink.style.color = 'blue';
    }
    else{
        useranchorlink.style.color = 'black';
    }


    
// =================================================================================


let useranchor = document.getElementById('useranchor');

customer.addEventListener('click',()=>{
    location.href = 'http://127.0.0.1:8000/APP/login/'
})

admin.addEventListener('click',()=>{
    location.href = 'http://127.0.0.1:8000/admin/'
});

if((window.location.href == 'https://jayakara.pythonanywhere.com/APP/user/') || (window.location.href == 'http://127.0.0.1:8000/APP/register/') || (window.location.href == 'http://127.0.0.1:8000/APP/login/')){
    useranchor.style.color = '#1D63FF';
}

else{
    useranchor.style.color = 'black';
}