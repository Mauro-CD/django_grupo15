let menu = document.getElementById('menu-ao');
const xhr = new XMLHttpRequest();
xhr.open('GET', '/static/sub-pages/menu.html');
xhr.setRequestHeader('Content-Type', 'text/plain');
xhr.send();
xhr.onload = function (data) {
    menu.innerHTML = data.currentTarget.response;
};

function showMenu(show) {
    if (show) {
        document.getElementById("menuC").style.display = "none";
        document.getElementById("menuG").style.display = "block";
    } else {
        document.getElementById("menuC").style.display = "block";
        document.getElementById("menuG").style.display = "none";
    }
 }

 console.log("menu2")