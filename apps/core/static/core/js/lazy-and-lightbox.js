// lazy-and-lightbox.js
document.addEventListener("DOMContentLoaded", function () {
  // Initialize GLightbox
  try {
    window._glight = GLightbox({
      selector: '.glightbox',
      touchNavigation: true,
      loop: true,
      plyr: { css: 'https://cdn.plyr.io/3.7.2/plyr.css', js: 'https://cdn.plyr.io/3.7.2/plyr.min.js' },
    });
  } catch (e) {
    console.warn("GLightbox init failed:", e);
  }

  // Lazy loading via IntersectionObserver for images with data-src
  const lazyImages = Array.from(document.querySelectorAll('img[data-src]'));

  function loadImage(img) {
    if (!img) return;
    // set src from data-src
    img.src = img.dataset.src;
    if (img.dataset.srcset) img.srcset = img.dataset.srcset;
    img.removeAttribute('data-src');
    img.classList.add('loaded');
  }

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          loadImage(entry.target);
          obs.unobserve(entry.target);
        }
      });
    }, { rootMargin: "200px 0px", threshold: 0.01 });

    lazyImages.forEach(img => observer.observe(img));
  } else {
    // fallback: load immediately
    lazyImages.forEach(img => loadImage(img));
  }

  // Optional: re-init lightbox when images are loaded (useful if GLightbox is initialized before images)
  document.addEventListener('glightbox_reload', function () {
    if (window._glight && typeof window._glight.reload === 'function') {
      window._glight.reload();
    }
  });
});
