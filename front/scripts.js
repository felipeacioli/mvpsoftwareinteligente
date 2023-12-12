/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/amostras';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.amostras.forEach(item => insertList(
                                                item.numero,
                                                item.ph,
                                                item.hardness,
                                                item.solids = solids,
                                                item.chloramines,
                                                item.sulfate,
                                                item.conductivity,
                                                item.organic_carbon,
                                                item.trihalomethanes,
                                                item.turbidity,
                                                item.outcome
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputnumero, inputPh, inputHardness, inputSolids, inputChloramines,
                        inputSulfate, inputConductivity, inputOrganic_carbon,
                        inputTrihalomethanes, inputTurbidity
                        ) => {
    
  const formData = new FormData();
  formData.append('numero', inputnumero);
  formData.append('ph', inputPh);
  formData.append('Hardness', inputHardness);
  formData.append('Solids', inputSolids);
  formData.append('Chloramines', inputChloramines);
  formData.append('Sulfate', inputSulfate);
  formData.append('Conductivity', inputConductivity);
  formData.append('Organic_carbon', inputOrganic_carbon);
  formData.append('Trihalomethanes', inputTrihalomethanes);
  formData.append('Turbidity', inputTurbidity);

  let url = 'http://127.0.0.1:5000/amostra';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/amostra?numero='+item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
    
  let inputnumero = document.getElementById("newnumero").value;
  let inputPh = document.getElementById("newPh").value;
  let inputHardness = document.getElementById("newHardness").value;
  let inputSolids = document.getElementById("newSolids").value;
  let inputChloramines = document.getElementById("newChloramines").value;
  let inputSulfate = document.getElementById("newSulfate").value;
  let inputConductivity = document.getElementById("newConductivity").value;
  let inputOrganic_carbon = document.getElementById("newOrganic_carbon").value;
  let inputTrihalomethanes = document.getElementById("newTrihalomethanes").value;
  let inputTurbidity = document.getElementById("newTurbidity").value;

  // Verifique se o nome do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5000/amostra?numero=${inputnumero}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.amostras && data.amostras.some(item => item.numero === inputnumero)) {
        alert("O paciente já está cadastrado.\nCadastre o paciente com um nome diferente ou atualize o existente.");
      } else if (isNaN (inputnumero) || isNaN(inputPh) || isNaN(inputHardness) || isNaN(inputSolids) || isNaN(inputChloramines) || isNaN(inputSulfate) || isNaN(inputConductivity) || isNaN(inputOrganic_carbon) || isNaN(inputTrihalomethanes) || isNaN(inputTurbidity)) {
        alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputnumero, inputPh, inputHardness, inputSolids, inputChloramines, inputSulfate, inputConductivity, inputOrganic_carbon, inputTrihalomethanes, inputTurbidity); 
        postItem(inputnumero, inputPh, inputHardness, inputSolids, inputChloramines, inputSulfate, inputConductivity, inputOrganic_carbon, inputTrihalomethanes, inputTurbidity); 
        alert("Item adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (numero, Ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity, outcome) => {
  var item = [numero, Ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity, outcome];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);

  document.getElementById("newnumero").value = "";
  document.getElementById("newPh").value = "";
  document.getElementById("newHardness").value = "";
  document.getElementById("newSolids").value = "";
  document.getElementById("newChloramines").value = "";
  document.getElementById("newSulfate").value = "";
  document.getElementById("newConductivity").value = "";
  document.getElementById("newOrganic_carbon").value = "";
  document.getElementById("newTrihalomethanes").value = "";
  document.getElementById("newTurbidity").value = "";

  removeElement();
}