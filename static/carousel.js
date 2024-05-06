// carousel.js
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js"></script>
$(document).ready(function(){
    $('#properties-slider').slick({
        slidesToShow: 3, // Adjust the number of visible slides as needed
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 500, // Adjust autoplay speed as needed
        dots: true, // Add navigation dots
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    });
});
