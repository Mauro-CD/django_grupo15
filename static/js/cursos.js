let listado = document.getElementById('cursos-lista');

//fetch('/static/json/cursos.json', {
fetch('https://maurocd.pythonanywhere.com/courses', {
    method: 'GET',
    headers: {
        'Accept': 'application/json',
    },
})
   .then(response => response.json())
   .then(response => loadCourse(response))
   .catch(err => {
    console.error(err);
    this.error=true
    })
   

function ordenarAsc(p_array_json, p_key) {
    p_array_json.sort(function (a, b) {
        return a[p_key] > b[p_key];
    });
    
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

function loadCourse(cursos) {
    cursos=sortJSON(cursos, 'name', 'asc');
    for (let i = 0; i < cursos.length; i++) {
        let a = `<a>`
        let name = `<h3 id=nameCurso${i} class="title-course">${cursos[i].name}</h3>`;
        let image = `<p id=image type="button" ><img id=imageList onclick="GetCourse('${cursos[i].name}','${cursos[i].id}')" src="${cursos[i].image}"></p>`;
        let description = `<p id=description>${cursos[i].description}</p>`;
        //let boton = `<p type="button" onclick="cambiar('${cursos[i].Descripcion}')"><img src="${cursos[i].Imagen}"></p>`
        let af = `</a>`;
        listado.innerHTML += `<li >${ a +  name + image + description + af}</li>`;
    };
}


