let cate = document.getElementById('cate');

let nav = document.getElementById('navbar');

let cateanchor1 = document.getElementById('cateanchor1');



let applecate1 = document.getElementById('applecate1');
let onepluscate1 = document.getElementById('onepluscate1');
let samsungcate1 = document.getElementById('samsungcate1');
let redmicate1 = document.getElementById('redmicate1');
let realmecate1 = document.getElementById('realmecate1');

let totalc1 = document.getElementById('totalc1');
let totalc12 = document.getElementById('totalc12');
let totalc13 = document.getElementById('totalc13');
let totalc14 = document.getElementById('totalc14');
let totalc15 = document.getElementById('totalc15');

// console.log(cateanchor1);

if((window.location.href == 'http://127.0.0.1:8000/AppleApp/categories/apple/') || (window.location.href == 'http://127.0.0.1:8000/OneplusApp/categories/oneplus/') || (window.location.href == 'http://127.0.0.1:8000/SamsungApp/categories/samsung/') || (window.location.href == 'http://127.0.0.1:8000/RedmiApp/categories/redmi/') || (window.location.href == 'http://127.0.0.1:8000/RealmeApp/categories/realme/')){
    cateanchor1.style.color = '#1D63FF';
}

else{
    cateanchor1.style.color = 'black';
}

// console.log(cate.getBoundingClientRect().top);

window.addEventListener('scroll',()=>{
    if(cate.getBoundingClientRect().top<0){
        nav.style.cssText = 'box-shadow:0px 0px 25px black; background-color:white';
    }
    else{
        nav.style.backgroundColor = '#FFCE32';
        nav.style.cssText = 'box-shadow:none';
    }
})




applecate1.addEventListener('click',()=>{
    location.href = 'http://127.0.0.1:8000/AppleApp/categories/apple/';

    // console.log(true);
    totalc1.style.display = 'block';
    totalc12.style.display = 'none';
    totalc13.style.display = 'none';
    totalc14.style.display = 'none';
    totalc15.style.display = 'none';
})

onepluscate1.addEventListener('click',()=>{
    location.href = 'http://127.0.0.1:8000/OneplusApp/categories/oneplus/';

    totalc1.style.display = 'none';
    totalc12.style.display = 'block';
    totalc13.style.display = 'none';
    totalc14.style.display = 'none';
    totalc15.style.display = 'none';

})

samsungcate1.addEventListener('click',()=>{
    location.href = 'http://127.0.0.1:8000/SamsungApp/categories/samsung/';

    totalc1.style.display = 'none';
    totalc13.style.display = 'block';
    totalc12.style.display = 'none';
    totalc14.style.display = 'none';
    totalc15.style.display = 'none';

})

redmicate1.addEventListener('click',()=>{
    location.href = 'http://127.0.0.1:8000/RedmiApp/categories/redmi/';

    totalc1.style.display = 'none';
    totalc14.style.display = 'block';
    totalc12.style.display = 'none';
    totalc13.style.display = 'none';
    totalc15.style.display = 'none';

})

realmecate1.addEventListener('click',()=>{
    location.href = 'http://127.0.0.1:8000/RealmeApp/categories/realme/';

    totalc1.style.display = 'none';
    totalc15.style.display = 'block';
    totalc12.style.display = 'none';
    totalc13.style.display = 'none';
    totalc14.style.display = 'none';

})

if(window.location.href == 'http://127.0.0.1:8000/AppleApp/categories/apple/'){
    applecate1.style.border = 'solid 3px #1D63FF';
    onepluscate1.style.border = 'none';
    samsungcate1.style.border = 'none';
    redmicate1.style.border = 'none';
    realmecate1.style.border = 'none';
}
else if(window.location.href == 'http://127.0.0.1:8000/OneplusApp/categories/oneplus/'){
    applecate1.style.border = 'none';
    onepluscate1.style.border = 'solid 3px #1D63FF';
    samsungcate1.style.border = 'none';
    redmicate1.style.border = 'none';
    realmecate1.style.border = 'none';
}

else if(window.location.href == 'http://127.0.0.1:8000/SamsungApp/categories/samsung/'){
    applecate1.style.border = 'none';
    onepluscate1.style.border = 'none';
    samsungcate1.style.border = 'solid 3px #1D63FF';
    redmicate1.style.border = 'none';
    realmecate1.style.border = 'none';
}

else if(window.location.href == 'http://127.0.0.1:8000/RedmiApp/categories/redmi/'){
    applecate1.style.border = 'none';
    onepluscate1.style.border = 'none';
    samsungcate1.style.border = 'none';
    redmicate1.style.border = 'solid 3px #1D63FF';
    realmecate1.style.border = 'none';
}

else if(window.location.href == 'http://127.0.0.1:8000/RealmeApp/categories/realme/'){
    applecate1.style.border = 'none';
    onepluscate1.style.border = 'none';
    samsungcate1.style.border = 'none';
    redmicate1.style.border = 'none';
    realmecate1.style.border = 'solid 3px #1D63FF';
}

