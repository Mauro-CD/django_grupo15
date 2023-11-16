function search() {
    var input, filter, cards, card, title, i;
    input = document.getElementById("buscar");
    filter = input.value.toUpperCase();
    cards = document.getElementsByClassName("card");

    for (i = 0; i < cards.length; i++) {
        card = cards[i];
        title = card.querySelector(".card-title");

        if (title.innerText.toUpperCase().indexOf(filter) > -1) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }
    }

    // Cheque si los item no fueron encontrados
    var noResultsMessage = document.getElementById("noResultsMessage");
    if (cards.length > 0 && document.querySelectorAll('.card[style="display: none;"]').length === cards.length) {
        // Si las cards estan ocultas, mostrar que no hay resultado
        noResultsMessage.style.display = "block";
    } else {
        noResultsMessage.style.display = "none";
    }
}