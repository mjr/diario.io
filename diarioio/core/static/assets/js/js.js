var numeroFilhos

function attNumeroFilhos(){
  numeroFilhos = document.getElementById("objetivos").childElementCount;
  console.log(numeroFilhos);
}

function add_campo() {
    const divGroup = document.createElement('div')
    divGroup.className = 'row'

    const divInput = document.createElement('div')
    divInput.className = 'col-md-10'

    const inputObjetivo = document.createElement('input')
    inputObjetivo.type = 'text'
    inputObjetivo.className = 'form-control'
    inputObjetivo.placeholder = 'Indique o objetivo do dia'
    const divIcon = document.createElement('div')
    divIcon.className = 'col-md-2'
    divIcon.setAttribute("onclick","remove_campo(this)")


    const spanIcon = document.createElement('span')
    spanIcon.className = 'ti-trash'

    divInput.appendChild(inputObjetivo)
    divIcon.appendChild(spanIcon)
    divGroup.appendChild(divInput)
    divGroup.appendChild(divIcon)
    console.log(divGroup)

    document.getElementById('objetivos').appendChild(divGroup)
    attNumeroFilhos();
    //document.getElementById('objetivos').innerHTML += '<div class="row"><div class="col-md-10"><input type="text" class="form-control" placeholder="Indique o objetivo do dia"></input></div><div class="col-md-2 icone-grande" onclick="remove_campo(this)"><span class="ti-trash"></span></div></div>';
};

function remove_campo(objeto) {
  attNumeroFilhos();
  console.log(numeroFilhos);
  if (numeroFilhos > 2) {
    objeto.parentNode.remove()
  }else{
    sweetAlert("Oops...", "Você precisa ter ao menos 1 objetivo!", "warning");
  }
};

function chegar(){
  document.getElementById('divCheguei').style.display = 'none';
  document.getElementById('divObjetivos').style.display = 'block';
}
