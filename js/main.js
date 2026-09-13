// Arrow Cup site — small progressive-enhancement helpers
document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', links.classList.contains('open'));
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); });
    });
  }

  // Highlight current nav link
  var here = (location.pathname.split('/').pop() || 'index.html');
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    var target = a.getAttribute('href');
    if (target === here || (here === '' && target === 'index.html')) {
      a.classList.add('active');
    }
  });

  // Gallery filter
  var filterButtons = document.querySelectorAll('.filter-btn');
  var galleryItems = document.querySelectorAll('.gallery-item');
  if (filterButtons.length) {
    filterButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        filterButtons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var f = btn.getAttribute('data-filter');
        galleryItems.forEach(function (item) {
          var show = f === 'all' || item.getAttribute('data-category') === f;
          item.style.display = show ? '' : 'none';
        });
      });
    });
  }

  // Lightbox
  var lightbox = document.querySelector('.lightbox');
  if (lightbox && galleryItems.length) {
    var lbImg = lightbox.querySelector('img');
    var visibleList = [];
    var currentIndex = 0;

    function openAt(index) {
      visibleList = Array.prototype.filter.call(galleryItems, function (i) {
        return i.style.display !== 'none';
      });
      currentIndex = visibleList.indexOf(index);
      if (currentIndex === -1) currentIndex = 0;
      show(currentIndex);
      lightbox.classList.add('open');
    }
    function show(i) {
      var item = visibleList[i];
      if (!item) return;
      var img = item.querySelector('img');
      lbImg.src = img.src;
      lbImg.alt = img.alt;
    }
    galleryItems.forEach(function (item) {
      item.addEventListener('click', function () { openAt(item); });
    });
    lightbox.querySelector('.lightbox-close').addEventListener('click', function () {
      lightbox.classList.remove('open');
    });
    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox) lightbox.classList.remove('open');
    });
    lightbox.querySelector('.lightbox-prev').addEventListener('click', function () {
      currentIndex = (currentIndex - 1 + visibleList.length) % visibleList.length;
      show(currentIndex);
    });
    lightbox.querySelector('.lightbox-next').addEventListener('click', function () {
      currentIndex = (currentIndex + 1) % visibleList.length;
      show(currentIndex);
    });
    document.addEventListener('keydown', function (e) {
      if (!lightbox.classList.contains('open')) return;
      if (e.key === 'Escape') lightbox.classList.remove('open');
      if (e.key === 'ArrowLeft') lightbox.querySelector('.lightbox-prev').click();
      if (e.key === 'ArrowRight') lightbox.querySelector('.lightbox-next').click();
    });
  }

  // Contact form (static hosting — no backend by default)
  var form = document.querySelector('.contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      var action = form.getAttribute('action') || '';
      if (action.indexOf('formspree.io') === -1) {
        // No form backend configured yet — show a friendly message instead of failing silently.
        e.preventDefault();
        var success = document.querySelector('.form-success');
        if (success) {
          success.textContent = 'Thanks! This form isn’t connected to an inbox yet — please email us directly for now (see contact info) while we finish setup.';
          success.classList.add('show');
        }
      }
    });
  }

  // Footer year
  var yearEl = document.querySelector('[data-year]');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});
