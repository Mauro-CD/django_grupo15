function cancelPayment() {
    // Implementar cualquier lógica necesaria antes de redirigir a la página anterior
    window.history.back();
}

function confirmPayment() {
    // Implementar logica de confirmacion de pago
    var creditCardNumber = document.getElementById("creditCardNumber").value;
    var expiryDate = document.getElementById("expiryDate").value;
    var cvv = document.getElementById("cvv").value;

    // Ejecutar validacion
    if (creditCardNumber.length !== 16 || !expiryDate.match(/^(0[1-9]|1[0-2])\/[0-9]{4}$/) || cvv.length !== 3) {
        document.getElementById("paymentMessage").innerText = "Informacion de pago invalida. Chequea los datos ingresados.";
        return;
    }

    // Mensaje de pago(simulacion)
    document.getElementById("paymentMessage").innerText = "Pago realizado con exito! Gracias por tu compra";
}