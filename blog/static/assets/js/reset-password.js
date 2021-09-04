const container = document.querySelector(".container");

function myFunction2(){
    const x = document.getElementById('myInput2');
    const y = document.getElementById('hide111');
    const z = document.getElementById('hide222');

    if(x.type === 'password'){
        x.type = 'text';
        y.style.display = 'block';
        z.style.display = 'none';
    }
    else{
        x.type = 'password';
        y.style.display = 'none';
        z.style.display = 'block';
    }
}
