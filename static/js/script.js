// toggle icon navbar
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec =>{
        let top = window.scrollY;
        let offset = sec.offsetTop-150;
        let height =sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top>= offset &&top< offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        };
    });
    // Nav-bar
    let header = document.querySelector('header')
    header.classList.toggle('sticky', window.scrollY > 100);
    // When scroll remove toggle icon and navbar
    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');
};
ScrollReveal({ 
    reset: true,
    distance: '80px',
    duration: 2000,
    delay: 200
});
ScrollReveal().reveal('.home-content, .heading', { origin:  'top'});
ScrollReveal().reveal('.home-img', { origin:  'right'});
ScrollReveal().reveal('.contact form', { origin:  'bottom'});

// typing js

const typed = new Typed('.multiple-text', {
    strings: ['Data Scientist','Physicist', 'Mechanical Engineer'],
    typeSpeed: 100,
    backSpeed: 80,
    backDelay: 500,
    loop:true
  });


