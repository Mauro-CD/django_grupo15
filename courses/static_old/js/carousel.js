let carousel = document.getElementById('cursos-carousel');

fetch('/static/json/cursos.json', {
    method: 'GET',
    headers: {
        'Accept': 'application/json',
    },
})
   .then(response => response.json())
   .then(response => loadCarousel(response))
   .catch(err => {
    console.error(err);
    this.error=true
    })
   


function verificaAnterior(i, l) {
    let resultado = Number
    if ( i < 1 ) {
        return resultado = l
    } else { 
        return resultado = i-1
    }

}

function verificaSiguiente(i, l) {
    let resultado = Number
    if ( i < l ) {
        return resultado = i+1
    } else { 
        return resultado = 0
    }

}

function sortJSON(data, key, orden) {
    return data.sort(function (a, b) {
        var x = a[key],
        y = b[key];

        if (orden === 'asc') {
            return ((x < y) ? -1 : ((x > y) ? 1 : 0));
        }

        if (orden === 'desc') {
            return ((x > y) ? -1 : ((x < y) ? 1 : 0));
        }
    });
}

function loadCarousel(cursos) {
    // Clear the existing content
    carousel.innerHTML = '';

    cursos = sortJSON(cursos, 'views', 'desc');
    let top = 5;
    let ol1 = `<ol class="carousel__viewport">`;
    let ol2 = `<aside class="carousel__navigation"><ol class="carousel__navigation-list">`;
    if (cursos.length < top) {
        top = cursos.length;
    }
    for (let i = 0; i < top; i++) {
        let nombre = `<p class="nameCourse">${cursos[i].name}</p>`;
        let li = `<li onclick="GetCourse('${cursos[i].name}','${cursos[i].id}')" id="carousel__slide${i}" tabindex="0" class="carousel__slide">`;
        let image = `<img id="imagecarousel" src="${cursos[i].image}">`; // Fixed the ID here
        let ni = verificaAnterior(i, cursos.length - 1);
        let nf = verificaSiguiente(i, cursos.length - 1);
        let div = `<div class="carousel__snapper"><a href="#carousel__slide${ni}" class="carousel__prev">Anterior</a><a href="#carousel__slide${nf}" class="carousel__next">Siguiente</a></div>`;
        ol1 = ol1 + `${li + nombre + image + div}</li>`;
        ol2 = ol2 + `<li class="carousel__navigation-item"><a href="#carousel__slide${i}" class="carousel__navigation-button">Ir a diapositiva ${i}</a></li>`;
    }
    ol1 = ol1 + `</ol>`;
    ol2 = ol2 + `</aside>`;
    carousel.innerHTML += `<section class="carousel" aria-label="Galeria">` + ol1 + ol2 + `</section>`;
}