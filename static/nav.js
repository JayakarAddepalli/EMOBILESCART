let navicon = document.getElementById('navicondiv');
let anchor = document.getElementById('anchor');
let cross = document.getElementById('crossdiv');


navicon.addEventListener('click',()=>{
    anchor.style.visibility = 'visible';
    cross.style.visibility = 'visible';
})

cross.addEventListener('click',()=>{
    anchor.style.visibility = 'hidden';
    cross.style.visibility = 'hidden';
})