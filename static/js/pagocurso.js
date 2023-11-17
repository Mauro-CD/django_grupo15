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
    var id = document.getElementById("idUsuario").innerText;
    var email = document.getElementById("emailUsuario").innerText;

    // Ejecutar validación
    if (creditCardNumber.length !== 16 || !expiryDate.match(/^(0[1-9]|1[0-2])\/[0-9]{4}$/) || cvv.length !== 3) {
        document.getElementById("paymentMessage").innerText = "Información de pago inválida. Verifica los datos ingresados.";
        return;
    }

    // Mensaje de pago (simulación)
    document.getElementById("paymentMessage").innerText = "Pago realizado con éxito. ¡Gracias por tu compra!";

    // Obtener parámetros de la URL
    var urlParams = new URLSearchParams(window.location.search);
    var cursoId = urlParams.get('curso_id');
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
        // También puedes mostrar un mensaje en la consola
        console.log('Compra confirmada para el curso:', cursoTitulo);
    }
}


// pagocurso.js
/*

document.addEventListener('DOMContentLoaded', function () {
    var urlParams = new URLSearchParams(window.location.search);
    var cursoId = urlParams.get('curso_id');
    var cursoTitulo = urlParams.get('curso_titulo');
    var cursoDocenteId = urlParams.get('curso_docente_id');

    // Check if the necessary parameters are present
    if (cursoId && cursoTitulo && cursoDocenteId) {
        console.log('Curso ID:', cursoId);
        console.log('Curso Titulo:', cursoTitulo);
        console.log('Curso Docente ID:', cursoDocenteId);

        // Display an alert with the information
        alert('Compra confirmada para el curso:\n\nID: ' + cursoId + '\nTitulo: ' + cursoTitulo + '\nDocente ID: ' + cursoDocenteId);
    }
});*/