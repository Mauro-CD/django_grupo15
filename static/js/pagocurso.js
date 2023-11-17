function cancelPayment() {
    // Implementar cualquier lógica necesaria antes de redirigir a la página anterior
    window.history.back();
}

function confirmPayment() {
    // Implementar lógica de confirmación de pago
    var creditCardNumber = document.getElementById("creditCardNumber").value;
    var expiryDate = document.getElementById("expiryDate").value;
    var cvv = document.getElementById("cvv").value;
    var nombre = document.getElementById("nombreUsuario").innerText;
    var apellido = document.getElementById("apellidoUsuario").innerText;
    var id = parseInt(document.getElementById("idUsuario").innerText);
    var email = document.getElementById("emailUsuario").innerText; 
    var matricula = parseInt(id) + 5000;
    // Ejecutar validación
    if (creditCardNumber.length !== 16 || !expiryDate.match(/^(0[1-9]|1[0-2])\/[0-9]{4}$/) || cvv.length !== 3) {
        document.getElementById("paymentMessage").innerText = "Información de pago inválida. Verifica los datos ingresados.";
        return;
    }

    // Mensaje de pago (simulación)
    document.getElementById("paymentMessage").innerText = "Pago realizado con éxito. ¡Gracias por tu compra!";

    // Componentes de la fecha en formato string simple
    const currentDate = new Date();
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth() + 1; 
    const day = currentDate.getDate();
    //componentes fecha en formato mas detallado
    var currentDate2 = new Date();
    // Formateo fecha en el formato del db
    var formattedDate =
    currentDate.getFullYear() +
    "-" +
    ((currentDate.getMonth() + 1) < 10 ? '0' : '') + (currentDate.getMonth() + 1) +
    "-" +
    (currentDate.getDate() < 10 ? '0' : '') + currentDate.getDate() +
    " " +
    (currentDate.getHours() < 10 ? '0' : '') + currentDate.getHours() +
    ":" +
    (currentDate.getMinutes() < 10 ? '0' : '') + currentDate.getMinutes() +
    ":" +
    (currentDate.getSeconds() < 10 ? '0' : '') + currentDate.getSeconds() +
    "." +
    (currentDate.getMilliseconds() < 10 ? '00' : (currentDate.getMilliseconds() < 100 ? '0' : '')) + currentDate.getMilliseconds() +
    "000" + 
    "+00";
    // Obtener parámetros de la URL
    var urlParams = new URLSearchParams(window.location.search);
    var cursoId = parseInt(urlParams.get('curso_id'));
    var cursoTitulo = urlParams.get('curso_titulo');
    var cursoDocenteId = urlParams.get('curso_docente_id');

    // Verificar si los parámetros necesarios están presentes
    if (cursoId && cursoTitulo && cursoDocenteId) {
        // Mostrar en la consola la información requerida
        console.log('Curso ID:', cursoId);
        console.log('Curso Título:', cursoTitulo);
        console.log('Curso Docente ID:', cursoDocenteId);
        console.log('Nombre:',nombre);
        console.log('Apellido:',apellido);
        console.log('Id:',id);
        console.log('Email:',email);
        console.log('Matricula:',matricula);
        console.log(`Current Date: ${day}/${month}/${year}`);
        console.log("fecha en formato",formattedDate);
        // También puedes mostrar un mensaje en la consola
        console.log('Compra confirmada para el curso:', cursoTitulo);
    }
}
