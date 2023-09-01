// Validación de formulario de SignUp
(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {

        let password = document.getElementById('floatingPassword');
        let password_ok = validar_password(password.value);        
        if (password_ok) {
          password.classList.remove("is-invalid");
          password.classList.add("is-valid");
        }else {
          password.classList.remove("is-valid");
          password.classList.add("is-invalid");
        }

        let password2 = document.getElementById('floatingPassword2');
        if (password.value == password2.value) {
          password2.classList.remove("is-invalid");
          password2.classList.add("is-valid");
        }else {
          password_ok = false;
          password2.classList.remove("is-valid");
          password2.classList.add("is-invalid");
        }

        if (!form.checkValidity() || !password_ok) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
      }, false)
    })
})()

let cumpleLongitud, cumpleMayus, cumpleNum, cumpleCarEspec;    
const longitud = 8;
const caracteresEspeciales = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~";
const numeros = "0123456789";

const validar_password = (password) => {
  if (password.length < longitud) {
    cumpleLongitud = false;
  } else if (password.length > 7) {
    cumpleLongitud = true;
  }

  if (password.toLowerCase() == password) {
    cumpleMayus = false;
  } else {
    cumpleMayus = true;
  }

  cumpleNum = false;
  for (let i = 0; i < password.length; i++) {
      for (let j = 0; j < numeros.length; j++) {
          if (password[i] == numeros[j]) {
            cumpleNum = true;
          }
      }
  }

  cumpleCarEspec = false;
  for (let i = 0; i < password.length; i++) {
      for (let j = 0; j < caracteresEspeciales.length; j++) {
          if (password[i] == caracteresEspeciales[j]) {
            cumpleCarEspec = true;
          }
      }
  }

  return cumpleLongitud == true && cumpleMayus  == true && cumpleNum  == true && cumpleCarEspec == true;
}

const sign_up = () => {
    let email = document.getElementById('floatingEmailInput').value;
    let nombre = document.getElementById('floatingNombreInput').value;
    let apellido = document.getElementById('floatingApellidoInput').value;    
    let password = document.getElementById('floatingPassword').value;
    
    let csrf_token = Cookies.get('csrftoken');

    axios.post('/signup/',
      {'nombre': nombre, 'apellido': apellido, 'email': email, 'password': password},
      {headers: {'X-CSRFToken': csrf_token}}
    ).then(resultado => {
        alert('El usuario se registró exitosamente. Inicie sesión.');
        document.location.href = '/login';
    }).catch(error => {
        let feedbackOtrasValidaciones = document.getElementById('feedbackOtrasValidaciones');
        feedbackOtrasValidaciones.classList.remove('d-none');        
        if (error.response.data) {
            feedbackOtrasValidaciones.innerHTML = error.response.data.msg;
        }else {
            feedbackOtrasValidaciones.innerHTML = 'No se pudo registrar el usuario. Ocurrió un problema de comunicación';
        }
    });
}