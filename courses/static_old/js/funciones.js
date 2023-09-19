let cursoSelecionado = document.getElementById('cursos-selecionado');
let popup = document.getElementById('popup');


popup.innerHTML = `
<h2>${localStorage.getItem("CourceName")}</h2>
<p>¿Desea ver el curso?</p>
<button class="button" onclick="clouseCourse('${localStorage.getItem("CourceID")}')">Ver</button>
<button class="button" onclick="clouseCourse()">Cancelar</button>
`;



function getCourse(id) {
   document.getElementById("principal").style.display = "none";
   fetch('/static/json/cursos.json', {
      method: 'GET',
      headers: {
          'Accept': 'application/json',
      },
  })
     .then(response => response.json())
     .then(response => load(response,id))

}

function load(curso,id) {
   let i = 0;
   let idNumber = Number(id);
   let exista = false;
   let cursoEncontrado = null;
   while (i < curso.length && !exista ) { 
      if (curso[i].id === idNumber) {
         exista = true;
         cursoEncontrado = curso[i];
      };
      i++
    }
    if (exista) {
      let cursoHTML = `<section><h2>${cursoEncontrado.name}</h2><ul>`
      for (let i = 0; i < cursoEncontrado.modulos.length; i++) {

         let li = `<li><h3>Modulo ${i+1}: ${cursoEncontrado.modulos[i].titulo}</h3><ul>`;
         cursoHTML = cursoHTML + li
         for (let n = 0; n < cursoEncontrado.modulos[i].contenido.length; n++) {

            let li = `<a>Leccion ${n+1}: ${cursoEncontrado.modulos[i].contenido[n]}</a>`;
            cursoHTML = cursoHTML + `<li>${li}</li>`
         }
         cursoHTML = cursoHTML + `</ul></li>`
      }
      cursoHTML = cursoHTML + `</ul></section>`;
      let pie = `<section><h2>Detalles del curso</h2><ul><li><strong>Instructor:</strong> ${cursoEncontrado.instructor}</li><li><strong>Duracion:</strong> ${cursoEncontrado.duracion}</li></ul><button class="button" name="Inscribirme" onclick="inscripcion(true)">Inscribirme en el curso</button><button class="button bottonCancel" name="cancelar" onclick="inscripcion(false)">Cancelar</button></section>`
      cursoSelecionado.innerHTML = cursoHTML + pie
      document.getElementById("secundario").style.display = "block";
    } else {
      document.getElementById("principal").style.display = "block";
      alert("No se encontro el curso")
    }
}

