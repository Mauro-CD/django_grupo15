// var elementos = document.getElementsByName("pregunta");

// for(var i=0; i<elementos.length; i++) {
//   console.log(" Elemento: " + elementos[i].value + "\n Seleccionado: " + elementos[i].checked);
// }

function registro() {
    let name = document.getElementById("name").value;
    let lastname = document.getElementById("lastname").value;
    let email = document.getElementById("email").value;
    let emailValidate = /[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-zA-Z]{2,4}/;
    let password = document.getElementById("password").value;
    let password2 = document.getElementById("password2").value;
    if (name.length > 1) {
        document.getElementById('invalidName').style.display="none";
    } else {
        document.getElementById('invalidName').style.display="block";
        return 1;
    }
    if (lastname.length > 1) {
        document.getElementById('invalidLastname').style.display="none";
    } else {
        document.getElementById('invalidLastname').style.display="block";
        return 1;
    }
    if (emailValidate.test(email)) {
        document.getElementById('invalidMail').style.display="none";
    } else {
        document.getElementById('invalidMail').style.display="block";
        return 1;
    }
    if ( password === password2 && password.length > 5 ) {
        document.getElementById('invalidPassword').style.display="none";
    } else {
        document.getElementById('invalidPassword').style.display="block";
        return 1;
    }
    window.alert("Muchas gracias por registrarse")
    document.formu.submit();
}
