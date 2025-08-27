document.addEventListener('DOMContentLoaded', function() {
    
    /**
     * Handles the navbar style change on scroll.
     */
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    /**
     * Highlights the active navigation link based on the current URL.
     */
    const navLinks = document.querySelectorAll('.nav-link');
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        // Use 'endsWith' for a more robust check, especially for the homepage.
        if (link.getAttribute('href') === currentPath || (currentPath === '/' && link.getAttribute('href').endsWith('peta-utama/'))) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }

        // Add ripple effect on click
        link.addEventListener('click', createRipple);
    });

    /**
     * Closes the mobile menu when a nav link is clicked.
     */
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const bsCollapse = new bootstrap.Collapse(navbarCollapse, { toggle: false });
    
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse.classList.contains('show')) {
                bsCollapse.hide();
            }
        });
    });

    /**
     * Creates a ripple effect on a clicked element.
     * @param {MouseEvent} event - The click event.
     */
    function createRipple(event) {
        const element = event.currentTarget;

        const ripple = document.createElement('span');
        ripple.classList.add('ripple-effect');
        
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = `${size}px`;
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        
        element.appendChild(ripple);
        
        // Clean up the ripple element after the animation ends
        ripple.addEventListener('animationend', () => {
            ripple.remove();
        });
    }
});