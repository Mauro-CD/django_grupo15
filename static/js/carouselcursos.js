// cargo data del json
fetch('/static/json/cursos2.json')
  .then(response => response.json())
  .then(data => {
    const carouselDiv = document.getElementById('carouselDiv');
    let currentIndex = 0;
    let interval;

    // funcion que actualiza el carrousel
    function updateCarousel() {
      const currentItem = data[currentIndex];
      carouselDiv.innerHTML = `
        <img src="${currentItem.imagePath}" alt="${currentItem.title}" style="border-radius: 10px;">
        <h2 id="cardbox"style="border-radius: 7px;">${currentItem.title}</h2>
      `;
    }

    //Funcion que inicia carrousel
    function startAutomaticCarousel() {
      interval = setInterval(() => {
        currentIndex = (currentIndex + 1) % data.length;
        updateCarousel();
      }, 7000);
    }

    // inicializo 
    updateCarousel();
    startAutomaticCarousel();

    // senal de next prev botones
    const nextButton = document.getElementById('nextButton');
    const prevButton = document.getElementById('prevButton');

    // Event listener para el next 
    nextButton.addEventListener('click', () => {
      currentIndex = (currentIndex + 1) % data.length;
      updateCarousel();
      clearInterval(interval); // Stop automatic carousel
      startAutomaticCarousel(); // Start it again
    });

    // Event listener para el previous
    prevButton.addEventListener('click', () => {
      currentIndex = (currentIndex - 1 + data.length) % data.length;
      updateCarousel();
      clearInterval(interval); // Stop automatic carousel
      startAutomaticCarousel(); // Start it again
    });
  })
  .catch(error => console.error('Error loading JSON:', error));
