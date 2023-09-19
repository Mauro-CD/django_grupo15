function valida() {
  let emailValidate = /[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-zA-Z]{2,4}/;
  if (document.contacto.name.value.length > 1) {
    document.getElementById('invalidName').style.display = "none";
  } else {
    document.getElementById('invalidName').style.display = "block";
    return 1;
  }

  if (emailValidate.test(document.contacto.email.value)) {
    document.getElementById('invalidMail').style.display = "none";
  } else {
    document.getElementById('invalidMail').style.display = "block";
    return 1;
  }

  telefono = document.contacto.telefono.value
  telefono = validarEntero(telefono)
  document.contacto.telefono.value = telefono
  if (telefono > 0) {
    document.getElementById('invalidPhone').style.display = "none";
  } else {
    document.getElementById('invalidPhone').style.display = "block";
    return 1;
  }

  if (document.contacto.message.value.length > 0) {
    document.getElementById('invalidMessage').style.display = "none";
  } else {
    document.getElementById('invalidMessage').style.display = "block";
    return 1;
  }
  alert("Muchas gracias por contactarse");
  document.contacto.submit();
}

function validarEntero(valor) {
  valor = parseInt(valor)

  if (isNaN(valor)) {
    return ""
  } else {
    return valor
  }
}