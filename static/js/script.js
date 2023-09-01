let provincias = [
    ['01', 'AZUAY'],
    ['02', 'BOLIVAR'],
    ['03', 'CAÑAR'],
    ['04', 'CARCHI'],
    ['05', 'COTOPAXI'],
    ['06', 'CHIMBORAZO'],
    ['07', 'EL ORO'],
    ['08', 'ESMERALDAS'],
    ['09', 'GUAYAS'],
    ['10', 'IMBABURA'],
    ['11', 'LOJA'],
    ['12', 'LOS RIOS'],
    ['13', 'MANABI'],
    ['14', 'MORONA SANTIAGO'],
    ['15', 'NAPO'],
    ['16', 'PASTAZA'],
    ['17', 'PICHINCHA'],
    ['18', 'TUNGURAHUA'],
    ['19', 'ZAMORA CHINCHIPE'],
    ['20', 'GALAPAGOS'],
    ['21', 'SUCUMBIOS'],
    ['22', 'ORELLANA'],
    ['23', 'SANTO DOMINGO DE LOS TSACHILAS'],
    ['24', 'SANTA ELENA']
];

let ciudades = [
    ['01', '01', 'CUENCA'],
    ['01', '02', 'GIRON'],
    ['01', '03', 'GUALACEO'],
    ['01', '04', 'NABON'],
    ['01', '05', 'PAUTE'],
    ['01', '06', 'PUCARA'],
    ['01', '07', 'SAN FERNANDO'],
    ['01', '08', 'SANTA ISABEL'],
    ['01', '09', 'SIGSIG'],
    ['01', '10', 'OÑA'],
    ['01', '11', 'CHORDELEG'],
    ['01', '12', 'EL PAN'],
    ['01', '13', 'SEVILLA DE ORO'],
    ['01', '14', 'GUACHAPALA'],
    ['01', '15', 'CAMILO PONCE ENRIQUEZ'],
    ['02', '01', 'GUARANDA'],
    ['02', '02', 'CHILLANES'],
    ['02', '03', 'CHIMBO'],
    ['02', '04', 'ECHEANDIA'],
    ['02', '05', 'SAN MIGUEL'],
    ['02', '06', 'CALUMA'],
    ['02', '07', 'LAS NAVES'],
    ['03', '01', 'AZOGUES'],
    ['03', '02', 'BIBLIAN'],
    ['03', '03', 'CAÑAR'],
    ['03', '04', 'LA TRONCAL'],
    ['03', '05', 'EL TAMBO'],
    ['03', '06', 'DELEG'],
    ['03', '07', 'SUSCAL'],
    ['04', '01', 'TULCAN'],
    ['04', '02', 'BOLIVAR'],
    ['04', '03', 'ESPEJO'],
    ['04', '04', 'MIRA'],
    ['04', '05', 'MONTUFAR'],
    ['04', '06', 'SAN PEDRO DE HUACA'],
    ['05', '01', 'LATACUNGA'],
    ['05', '02', 'LA MANA'],
    ['05', '03', 'PANGUA'],
    ['05', '04', 'PUJILI'],
    ['05', '05', 'SALCEDO'],
    ['05', '06', 'SAQUISILI'],
    ['05', '07', 'SIGCHOS'],
    ['06', '01', 'RIOBAMBA'],
    ['06', '02', 'ALAUSI'],
    ['06', '03', 'COLTA'],
    ['06', '04', 'CHAMBO'],
    ['06', '05', 'CHUNCHI'],
    ['06', '06', 'GUAMOTE'],
    ['06', '07', 'GUANO'],
    ['06', '08', 'PALLATANGA'],
    ['06', '09', 'PENIPE'],
    ['06', '10', 'CUMANDA'],
    ['07', '01', 'MACHALA'],
    ['07', '02', 'ARENILLAS'],
    ['07', '03', 'ATAHUALPA'],
    ['07', '04', 'BALSAS'],
    ['07', '05', 'CHILLA'],
    ['07', '06', 'EL GUABO'],
    ['07', '07', 'HUAQUILLAS'],
    ['07', '08', 'MARCABELI'],
    ['07', '09', 'PASAJE'],
    ['07', '10', 'PIÑAS'],
    ['07', '11', 'PORTOVELO'],
    ['07', '12', 'SANTA ROSA'],
    ['07', '13', 'ZARUMA'],
    ['07', '14', 'LAS LAJAS'],
    ['08', '01', 'ESMERALDAS'],
    ['08', '02', 'ELOY ALFARO'],
    ['08', '03', 'MUISNE'],
    ['08', '04', 'QUININDE'],
    ['08', '05', 'SAN LORENZO'],
    ['08', '06', 'ATACAMES'],
    ['08', '07', 'RIOVERDE'],
    ['08', '08', 'LA CONCORDIA'],
    ['09', '01', 'GUAYAQUIL'],
    ['09', '02', 'ALFREDO BAQUERIZO MORENO (JUJAN)'],
    ['09', '03', 'BALAO'],
    ['09', '04', 'BALZAR'],
    ['09', '05', 'COLIMES'],
    ['09', '06', 'DAULE'],
    ['09', '07', 'DURAN'],
    ['09', '08', 'EL EMPALME'],
    ['09', '09', 'EL TRIUNFO'],
    ['09', '10', 'MILAGRO'],
    ['09', '11', 'NARANJAL'],
    ['09', '12', 'NARANJITO'],
    ['09', '13', 'PALESTINA'],
    ['09', '14', 'PEDRO CARBO'],
    ['09', '16', 'SAMBORONDON'],
    ['09', '18', 'SANTA LUCIA'],
    ['09', '19', 'SALITRE (URBINA JADO)'],
    ['09', '20', 'SAN JACINTO DE YAGUACHI'],
    ['09', '21', 'PLAYAS'],
    ['09', '22', 'SIMON BOLIVAR'],
    ['09', '23', 'CORONEL MARCELINO MARIDUEÑA'],
    ['09', '24', 'LOMAS DE SARGENTILLO'],
    ['09', '25', 'NOBOL'],
    ['09', '27', 'GENERAL ANTONIO ELIZALDE'],
    ['09', '28', 'ISIDRO AYORA'],
    ['10', '01', 'IBARRA'],
    ['10', '02', 'ANTONIO ANTE'],
    ['10', '03', 'COTACACHI'],
    ['10', '04', 'OTAVALO'],
    ['10', '05', 'PIMAMPIRO'],
    ['10', '06', 'SAN MIGUEL DE URCUQUI'],
    ['11', '01', 'LOJA'],
    ['11', '02', 'CALVAS'],
    ['11', '03', 'CATAMAYO'],
    ['11', '04', 'CELICA'],
    ['11', '05', 'CHAGUARPAMBA'],
    ['11', '06', 'ESPINDOLA'],
    ['11', '07', 'GONZANAMA'],
    ['11', '08', 'MACARA'],
    ['11', '09', 'PALTAS'],
    ['11', '10', 'PUYANGO'],
    ['11', '11', 'SARAGURO'],
    ['11', '12', 'SOZORANGA'],
    ['11', '13', 'ZAPOTILLO'],
    ['11', '14', 'PINDAL'],
    ['11', '15', 'QUILANGA'],
    ['11', '16', 'OLMEDO'],
    ['12', '01', 'BABAHOYO'],
    ['12', '02', 'BABA'],
    ['12', '03', 'MONTALVO'],
    ['12', '04', 'PUEBLOVIEJO'],
    ['12', '05', 'QUEVEDO'],
    ['12', '06', 'URDANETA'],
    ['12', '07', 'VENTANAS'],
    ['12', '08', 'VINCES'],
    ['12', '09', 'PALENQUE'],
    ['12', '10', 'BUENA FE'],
    ['12', '11', 'VALENCIA'],
    ['12', '12', 'MOCACHE'],
    ['12', '13', 'QUINSALOMA'],
    ['13', '01', 'PORTOVIEJO'],
    ['13', '02', 'BOLIVAR'],
    ['13', '03', 'CHONE'],
    ['13', '04', 'EL CARMEN'],
    ['13', '05', 'FLAVIO ALFARO'],
    ['13', '06', 'JIPIJAPA'],
    ['13', '07', 'JUNIN'],
    ['13', '08', 'MANTA'],
    ['13', '09', 'MONTECRISTI'],
    ['13', '10', 'PAJAN'],
    ['13', '11', 'PICHINCHA'],
    ['13', '12', 'ROCAFUERTE'],
    ['13', '13', 'SANTA ANA'],
    ['13', '14', 'SUCRE'],
    ['13', '15', 'TOSAGUA'],
    ['13', '16', '24 DE MAYO'],
    ['13', '17', 'PEDERNALES'],
    ['13', '18', 'OLMEDO'],
    ['13', '19', 'PUERTO LOPEZ'],
    ['13', '20', 'JAMA'],
    ['13', '21', 'JARAMIJO'],
    ['13', '22', 'SAN VICENTE'],
    ['14', '01', 'MORONA'],
    ['14', '02', 'GUALAQUIZA'],
    ['14', '03', 'LIMON INDANZA'],
    ['14', '04', 'PALORA'],
    ['14', '05', 'SANTIAGO'],
    ['14', '06', 'SUCUA'],
    ['14', '07', 'HUAMBOYA'],
    ['14', '08', 'SAN JUAN BOSCO'],
    ['14', '09', 'TAISHA'],
    ['14', '10', 'LOGROÑO'],
    ['14', '11', 'PABLO SEXTO'],
    ['14', '12', 'CANTON TIWINTZA'],
    ['15', '01', 'TENA'],
    ['15', '03', 'ARCHIDONA'],
    ['15', '04', 'EL CHACO'],
    ['15', '07', 'QUIJOS'],
    ['15', '09', 'CARLOS JULIO AROSEMENA TOLA'],
    ['16', '01', 'PASTAZA'],
    ['16', '02', 'MERA'],
    ['16', '03', 'SANTA CLARA'],
    ['16', '04', 'ARAJUNO'],
    ['17', '01', 'QUITO'],
    ['17', '02', 'CAYAMBE'],
    ['17', '03', 'MEJIA'],
    ['17', '03', 'MEJIA'],
    ['17', '04', 'PEDRO MONCAYO'],
    ['17', '05', 'RUMIÑAHUI'],
    ['17', '07', 'SAN MIGUEL DE LOS BANCOS'],
    ['17', '08', 'PEDRO VICENTE MALDONADO'],
    ['17', '09', 'PUERTO QUITO'],
    ['18', '01', 'AMBATO'],
    ['18', '02', 'BAÑOS DE AGUA SANTA'],
    ['18', '03', 'CEVALLOS'],
    ['18', '04', 'MOCHA'],
    ['18', '05', 'PATATE'],
    ['18', '06', 'QUERO'],
    ['18', '07', 'SAN PEDRO DE PELILEO'],
    ['18', '08', 'SANTIAGO DE PILLARO'],
    ['18', '09', 'TISALEO'],
    ['19', '01', 'ZAMORA'],
    ['19', '02', 'CHINCHIPE'],
    ['19', '03', 'NANGARITZA'],
    ['19', '04', 'YACUAMBI'],
    ['19', '05', 'YANTZAZA (YANZATZA)'],
    ['19', '06', 'EL PANGUI'],
    ['19', '07', 'CENTINELA DEL CONDOR'],
    ['19', '08', 'PALANDA'],
    ['19', '09', 'PAQUISHA'],
    ['20', '01', 'SAN CRISTOBAL'],
    ['20', '02', 'ISABELA'],
    ['20', '03', 'SANTA CRUZ'],
    ['21', '01', 'LAGO AGRIO'],
    ['21', '02', 'GONZALO PIZARRO'],
    ['21', '03', 'PUTUMAYO'],
    ['21', '04', 'SHUSHUFINDI'],
    ['21', '05', 'SUCUMBIOS'],
    ['21', '06', 'CASCALES'],
    ['21', '07', 'CUYABENO'],
    ['22', '01', 'ORELLANA'],
    ['22', '02', 'AGUARICO'],
    ['22', '03', 'LA JOYA DE LOS SACHAS'],
    ['22', '04', 'LORETO'],
    ['23', '01', 'SANTO DOMINGO'],
    ['24', '01', 'SANTA ELENA'],
    ['24', '02', 'LA LIBERTAD'],
    ['24', '03', 'SALINAS'],
    ['90', '01', 'ZONAS NO DELIMITADAS'],
    ['90', '03', 'ZONAS NO DELIMITADAS'],
    ['90', '04', 'ZONAS NO DELIMITADAS']
];

// notacion flecha para definir funciones. reemplaza al << function cargarProvincias(){} >> desde ES6
const cargarProvincias = () => {
    let provSelect = document.getElementById("provinceSelect");

    let emptyOption = document.createElement('option');
    emptyOption.text = "Seleccione una provincia";
    emptyOption.disabled = true;
    emptyOption.selected = true;
    emptyOption.value = "00";
    provSelect.add(emptyOption);

    provincias.forEach(prov=>{
        let provOption = document.createElement('option');
        provOption.value = prov[0];
        provOption.text = prov[1];

        provSelect.add(provOption);
    })    
}

const cargarCiudades = () => {
    let provSelect = document.getElementById("provinceSelect");
    let codigoProvincia = provSelect.value;
    
    let ciudadSelect = document.getElementById("citySelect");
    ciudadSelect.innerHTML = "";

    let ciudadesDeProvinciaSel = ciudades.filter(ciudad => ciudad[0]===codigoProvincia);

    ciudadesDeProvinciaSel.forEach(ciudad=>{
        let ciudadOption = document.createElement('option');
        ciudadOption.value = ciudad[1];
        ciudadOption.text = ciudad[2];

        ciudadSelect.add(ciudadOption);
    });   
}


cargarProvincias();

// Este código JS aplica las validaciones al formulario vía Bootstrap JS
(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })   
})()