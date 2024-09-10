let currentSlide = 0;

function moveCarousel(direction) {
    const carousel = document.querySelector('.carousel');
    const cards = document.querySelectorAll('.card');
    const cardWidth = cards[0].offsetWidth + 40; // Include margin
    const totalCards = cards.length;
    const visibleCards = Math.floor(document.querySelector('.carousel-container').offsetWidth / cardWidth);

    currentSlide += direction;

    if (currentSlide < 0) {
        currentSlide = 0;
    } else if (currentSlide > totalCards - visibleCards) {
        currentSlide = totalCards - visibleCards;
    }

    const newTransform = -currentSlide * cardWidth;
    carousel.style.transform = `translateX(${newTransform}px)`;
}
