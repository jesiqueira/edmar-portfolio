const cards = document.querySelectorAll('.project-card')

function animateCards() {
  cards.forEach((card, index) => {
    const rect = card.getBoundingClientRect()
    if (rect.top < window.innerHeight - 50) {
      setTimeout(() => {
        card.classList.remove('opacity-0', 'translate-y-4')
        card.classList.add('opacity-100', 'translate-y-0')
      }, index * 120)
    }
  })
}

window.addEventListener('scroll', animateCards)
window.addEventListener('load', animateCards)
