
var links = document.querySelectorAll('nav ul li a');


for (var i = 0; i < links.length; i++) {
	links[i].addEventListener('click', function(e) {
		e.preventDefault();
		
		
		var href = this.getAttribute('href');
		
		
		var section = document.querySelector(href);
		
		
		section.scrollIntoView({ behavior: 'smooth' });
	});
}
