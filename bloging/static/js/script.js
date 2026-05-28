/* ==========================================================================
   techdesk - Custom JavaScript
   Lightweight enhancements: smooth scroll, navbar shadow, mobile menu close.
   ========================================================================== */

(function () {
    'use strict';

    // 1. Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId.length <= 1) return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // 2. Navbar shadow on scroll
    const navbar = document.querySelector('.td-navbar');
    if (navbar) {
        const toggleShadow = () => {
            if (window.scrollY > 10) {
                navbar.style.boxShadow = '0 1px 3px rgba(0,0,0,0.04)';
            } else {
                navbar.style.boxShadow = 'none';
            }
        };
        toggleShadow();
        window.addEventListener('scroll', toggleShadow, { passive: true });
    }

    // 3. Auto-close mobile menu on link tap
    const navCollapse = document.querySelector('#mainNav');
    if (navCollapse) {
        navCollapse.querySelectorAll('.nav-link').forEach((link) => {
            link.addEventListener('click', () => {
                if (navCollapse.classList.contains('show')) {
                    if (window.bootstrap && window.bootstrap.Collapse) {
                        const instance = window.bootstrap.Collapse.getInstance(navCollapse)
                            || new window.bootstrap.Collapse(navCollapse, { toggle: false });
                        instance.hide();
                    }
                }
            });
        });
    }

    // 4. Console signature
    console.log('%c</> techdesk', 'color:#059669;font-family:monospace;font-size:18px;font-weight:bold;', 'by devs, for devs.');
})();