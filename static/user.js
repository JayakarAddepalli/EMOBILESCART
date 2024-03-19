let customer = document.getElementById('customer');
let admin = document.getElementById('admin');

// let logout = document.getElementById('logout');

// x = document.cookie

// console.log(x);

// if(x != sessionid){
//     logout.style.display = 'block';
// }
// else if (x==null){
//     logout.style.display = 'none';
// }

let useranchor = document.getElementById('useranchor');

customer.addEventListener('click',()=>{
    location.href = 'http://127.0.0.1:8000/APP/login/'
})

admin.addEventListener('click',()=>{
    location.href = 'http://127.0.0.1:8000/admin/'
});

if((window.location.href == 'http://127.0.0.1:8000/APP/user/') || (window.location.href == 'http://127.0.0.1:8000/APP/register/') || (window.location.href == 'http://127.0.0.1:8000/APP/login/')){
    useranchor.style.color = '#1D63FF';
}

else{
    useranchor.style.color = 'black';
}