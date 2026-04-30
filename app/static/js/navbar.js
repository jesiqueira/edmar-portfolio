const navbar = document.getElementById('navbar')

window.addEventListener('scroll', () => {
  if (window.scrollY > 10) {
    navbar.classList.add('bg-slate-900/90', 'backdrop-blur', 'border-b', 'border-slate-800')
  } else {
    navbar.classList.remove('bg-slate-900/90', 'backdrop-blur', 'border-b', 'border-slate-800')
  }
})

const menuBtn = document.getElementById('menu-btn')
const mobileMenu = document.getElementById('mobile-menu')
const menuLines = menuBtn.querySelectorAll('span')
const menuLinks = mobileMenu.querySelectorAll('a')
const mobileCta = document.getElementById('mobile-cta')

menuBtn.addEventListener('click', () => {
  const isHidden = mobileMenu.classList.contains('hidden')

  if (isHidden) {
    // Mostrar menu
    mobileMenu.classList.remove('hidden')

    setTimeout(() => {
      mobileMenu.classList.remove('opacity-0', '-translate-y-4')
      mobileMenu.classList.add('opacity-100', 'translate-y-0')

      // Animação dos links
      menuLinks.forEach((link, index) => {
        link.style.transitionDelay = `${index * 120}ms`
        link.classList.remove('opacity-0', 'translate-y-2')
        link.classList.add('opacity-100', 'translate-y-0')
      })

      // CTA entra por último
      setTimeout(() => {
        mobileCta.classList.remove('opacity-0', 'translate-y-2')
        mobileCta.classList.add('opacity-100', 'translate-y-0')
      }, menuLinks.length * 120)
    }, 10)

    // Hambúrguer vira X
    menuLines[0].classList.add('rotate-45', 'translate-y-2')
    menuLines[1].classList.add('opacity-0')
    menuLines[2].classList.add('-rotate-45', '-translate-y-2')
  } else {
    // Ocultar menu
    mobileMenu.classList.add('opacity-0', '-translate-y-4')
    mobileMenu.classList.remove('opacity-100', 'translate-y-0')

    // Links somem juntos
    menuLinks.forEach((link) => {
      link.style.transitionDelay = '0ms'
      link.classList.add('opacity-0', 'translate-y-2')
      link.classList.remove('opacity-100', 'translate-y-0')
    })

    setTimeout(() => {
      mobileMenu.classList.add('hidden')
    }, 300)

    // X volta ao normal
    menuLines[0].classList.remove('rotate-45', 'translate-y-2')
    menuLines[1].classList.remove('opacity-0')
    menuLines[2].classList.remove('-rotate-45', '-translate-y-2')
  }
})
