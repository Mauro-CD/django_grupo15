let cursoSelecionado = document.getElementById('cursos-selecionado');
let popup = document.getElementById('popup');


popup.innerHTML = `
<h2>${localStorage.getItem("CourceName")}</h2>
<p>¿Desea ver el curso?</p>
<button class="button" onclick="clouseCourse('${localStorage.getItem("CourceID")}')">Ver</button>
<button class="button" onclick="clouseCourse()">Cancelar</button>
`;



// function getCourse(id) {
//    document.getElementById("principal").style.display = "none";
//    fetch('./json/cursos.json', {
//       method: 'GET',
//       headers: {
//           'Accept': 'application/json',
//       },
//   })
//      .then(response => response.json())
//      .then(response => load(response,id))

// }

// function load(curso,id) {
//    let i = 0;
//    let idNumber = Number(id);
//    let exista = false;
//    let cursoEncontrado = null;
//    while (i < curso.length && !exista ) { 
//       if (curso[i].id === idNumber) {
//          exista = true;
//          cursoEncontrado = curso[i];
//       };
//       i++
//     }
//     if (exista) {
//       let cursoHTML = `<section><h2>${cursoEncontrado.name}</h2><ul>`
//       for (let i = 0; i < cursoEncontrado.modulos.length; i++) {

//          let li = `<li><h3>Modulo ${i+1}: ${cursoEncontrado.modulos[i].titulo}</h3><ul>`;
//          cursoHTML = cursoHTML + li
//          for (let n = 0; n < cursoEncontrado.modulos[i].contenido.length; n++) {

//             let li = `<a>Leccion ${n+1}: ${cursoEncontrado.modulos[i].contenido[n]}</a>`;
//             cursoHTML = cursoHTML + `<li>${li}</li>`
//          }
//          cursoHTML = cursoHTML + `</ul></li>`
//       }
//       cursoHTML = cursoHTML + `</ul></section>`;
//       let pie = `<section><h2>Detalles del curso</h2><ul><li><strong>Instructor:</strong> ${cursoEncontrado.instructor}</li><li><strong>Duracion:</strong> ${cursoEncontrado.duracion}</li></ul><button class="button" name="Inscribirme" onclick="inscripcion(true)">Inscribirme en el curso</button><button class="button bottonCancel" name="cancelar" onclick="inscripcion(false)">Cancelar</button></section>`
//       cursoSelecionado.innerHTML = cursoHTML + pie
//       document.getElementById("secundario").style.display = "block";
//     } else {
//       document.getElementById("principal").style.display = "block";
//       alert("No se encontro el curso")
//     }
// }

function getCourse(id) {
   let url = 'https://maurocd.pythonanywhere.com/courses/' + id;
   document.getElementById("principal").style.display = "none";
   fetch(url, {
      method: 'GET',
      headers: {
         'Accept': 'application/json',
      },
   })
      .then(response => response.json())
      .then(response => load(response))

}

console.log("funciones")

function load(curso) {
   let url = 'https://maurocd.pythonanywhere.com/modulos/' + curso.id;
   let urlItems = 'https://maurocd.pythonanywhere.com/contenidos/' + curso.id;
   if (curso.id > 0) {
      cursoHTML = `<section><h2>${curso.name}</h2><ul>`
      fetch(url, {
         method: 'GET',
         headers: {
            'Accept': 'application/json',
         },
      })
         .then(modulos => modulos.json())
         .then(modulos => {

            fetch(urlItems, {
               method: 'GET',
               headers: {
                  'Accept': 'application/json',
               },
            })
               .then(items => items.json())
               .then(items => {

                  for (let i = 0; i < modulos.length; i++) {
                     let li = `<li><h3>Modulo ${i + 1}: ${modulos[i].titulo}</h3><ul>`;
                     cursoHTML = cursoHTML + li
                     let numeroItem = 1;
                     for (let n = 0; n < items.length; n++) {
                        if (items[n].modulo === modulos[i].id) {
                           let li = `<a>Leccion ${numeroItem}: ${items[n].item}</a>`;
                           cursoHTML = cursoHTML + `<li>${li}</li>`;
                           numeroItem = numeroItem + 1
                        }
                     }
                     cursoHTML = cursoHTML + `</ul></li>`
                  }
                  cursoHTML = cursoHTML + `</ul></section>`;
                  let pie = `<section><h2>Detalles del curso</h2><ul><li><strong>Instructor:</strong> ${curso.instructor}</li><li><strong>Duracion:</strong> ${curso.duracion}</li></ul><button class="button" name="Inscribirme" onclick="inscripcion(true)">Inscribirme en el curso</button><button class="button bottonCancel" name="cancelar" onclick="inscripcion(false)">Cancelar</button></section>`
                  
                  cursoSelecionado.innerHTML = cursoHTML + pie
                  
                  document.getElementById("secundario").style.display = "block";
                  cursoHTML = cursoHTML + `</ul></li>`
               })
               .catch(err => {
                  console.error(err);
                  this.error = true
               })
         })
         .catch(err => {
            console.error(err);
            this.error = true
         });
      // viewsUp(curso)
   } else {
      document.getElementById("principal").style.display = "block";
      alert("No se encontro el curso")
   }
}

// function viewsUp(curso) {
//    let url = 'https://maurocd.pythonanywhere.com/courses/'+curso.id;
//    let curso2 = {
//       name: curso.name,
//       image: curso.imagen,
//       description: curso.description,
//       instructor: curso.instructor,
//       duracion: curso.duracion,
//       views: curso.views + 1
//   }

//    let options = {
//       body: JSON.stringify(curso2),
//       method: 'PUT',
//       headers: { 'Content-Type': 'application/json' }
//   }
//   fetch(url, options)
//       .then(function () {
//       })
//       .catch(err => {
//           console.error(err);
//           alert("Error al Modificar")
//       })
// }

function inscripcion(value) {
   if (localStorage.getItem("User") !== null) {
      // alert("Se inscribe al curso");
      login(true, value);
   } else {
      login(false, value);
   }
   document.getElementById("secundario").style.display = "none";
   document.getElementById("principal").style.display = "block";
}

function menuLogin() {
   if (localStorage.getItem("User") !== null) {
      // alert("Se inscribe al curso");
      login(true, true);
   } else {
      login(false, true);
   };
}

function login(login, inscribe) {
   if (inscribe) {
      window.location.href = "#openModal";
      popup.innerHTML = `
      <h2>${login ? "Validar clave" : "Iniciar sesión"}</h2>
      <div>
         <label for="usuario">Usuario:</label>
         <i class=""></i>
         ${login
            ? "<a class='formInput hold' type='text' id='user' name='user'>" + localStorage.getItem("User") + "</a>"
            : "<input class='formInput' type='text' id='user' name='user' placeholder='Nombre' minlength='1' required/>"
         }
         
         <div class="error"></div>
      </div>
      <div>
         <label for="password">Contraseña</label>
         <input class="formInput" type="password" id="password" name="password" placeholder="Ingresar contraseña" minlength="1" required/>
         <div class="error"></div>
      </div>
      <p id="invalidUser"></p>
      <button class="button" id="btn" value="loginValidate" onclick="loginValidate(${menu ? true : false})">Ingresar</button>
      `;
   }

}

function loadCourse(cursos) {
   for (let i = 0; i < cursos.length; i++) {
      let visitas = cursos[i].views
      if (visitas > 2) {
         let a = `<a href="#">`
         let name = `<h3>${cursos[i].name}</h3>`;
         let image = `<p type="button" onclick="cambiar('${cursos[i].description}')"><img src="${cursos[i].image}"></p>`;
         let description = `<p>${cursos[i].description}</p>`;
         //let boton = `<p type="button" onclick="cambiar('${cursos[i].Descripcion}')"><img src="${cursos[i].Imagen}"></p>`
         let af = `</a>`;
         listado.innerHTML += `<li>${a + name + image + description + af}</li>`;
      }
   };
}


function search() {
   let display, input, filter, lista, li, i, txtValue;
   input = document.getElementById("buscar");
   filter = input.value.toUpperCase();
   lista = document.getElementById("prueba");
   li = lista.getElementsByTagName("li");

   for (i = 0; i < li.length; i++) {
      display = "none";
      h3 = li[i].getElementsByTagName("h3")[0];
      if (h3) {
         txtValue = h3.textContent || h3.innerText;
         if (txtValue.toUpperCase().indexOf(filter) > -1) {
            display = "";
         }
      }
      li[i].style.display = display;
   }
}


function GetCourse(course, id) {
   localStorage.setItem("CourceName", course);
   localStorage.setItem("CourceID", id);
   window.location.href = "#openModal";
   popup.innerHTML = `
   <h2>${course}</h2>
   <p>¿Desea ver el curso?</p>
   <button class="button" onclick="clouseCourse('${id}')">Ver</button>
   <button class="button" onclick="clouseCourse()">Cancelar</button>
   `;
}

function clouseCourse(id) {
   // localStorage.removeItem("CourceID");
   // localStorage.removeItem("CourceName");
   if (id !== undefined) {
      getCourse(id);
   }
   window.location.href = "#couse";
}

function loginValidate(menu) {
   let id = true;
   let user;
   let password = document.getElementById("password").value

   console.log(user, password);
   if (localStorage.getItem("User") !== null) {
      user = localStorage.getItem("User");
   } else {
      user = document.getElementById("user").value
   }
   if (user.length > 0 && password.length > 0) {
      getUser(user, password, menu)
   } else {
      window.alert("Se debe ingresar usuario y password")
      // window.location.href = "#couse";
   }
}

function getUser(user, password, menu) {
   if (user === "admin" && password === "admin") {
      localStorage.setItem("User", user);
      if (!menu) {
         window.alert("se Inscribió al curso")
      } else {
         window.alert("Bienvenido")
      }
      window.location.href = "#couse";
   } else {
      // window.alert("usuario inexistente")
      document.getElementById('invalidUser').style.display = "block";
      document.getElementById('invalidUser').style.breakBefore.textContent = "block";
   }
}