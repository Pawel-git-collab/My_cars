let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";

}
// Start slideshow
    function startSlideshow() {
        intervalId = setInterval(showSlides, 5000); // Change slide every 5 seconds
    }

    // Stop slideshow
    function stopSlideshow() {
        clearInterval(intervalId);
    }

    // Start slideshow on page load
    window.onload = function () {
        startSlideshow();
    };

    // Add click event listener to stop slideshow
    const slideshowContainer = document.querySelector('.slideshow-container');
    slideshowContainer.addEventListener('click', function() {
        stopSlideshow();


    });