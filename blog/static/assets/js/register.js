const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});


function myFunction(){
  const x = document.getElementById('myInput');
  const y = document.getElementById('hide1');
  const z = document.getElementById('hide2');

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

function myFunction1(){
  const x = document.getElementById('myInput1');
  const y = document.getElementById('hide11');
  const z = document.getElementById('hide22');

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