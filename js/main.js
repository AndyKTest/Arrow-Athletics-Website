// Arrow Athletics — small progressive-enhancement helpers
document.addEventListener('DOMContentLoaded', function () {

  /* ---- Mobile nav ---- */
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---- Gallery filtering ---- */
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

  /* ---- Lightbox ---- */
  var lightbox = document.querySelector('.lightbox');
  if (lightbox && galleryItems.length) {
    var lbImg = lightbox.querySelector('img');
    var visible = [];
    var index = 0;

    function render(i) {
      var item = visible[i];
      if (!item) return;
      var img = item.querySelector('img');
      lbImg.src = img.src;
      lbImg.alt = img.alt;
    }

    function openFrom(item) {
      visible = Array.prototype.filter.call(galleryItems, function (i) {
        return i.style.display !== 'none';
      });
      index = Math.max(0, visible.indexOf(item));
      render(index);
      lightbox.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function close() {
      lightbox.classList.remove('open');
      document.body.style.overflow = '';
    }

    galleryItems.forEach(function (item) {
      item.addEventListener('click', function () { openFrom(item); });
    });

    lightbox.querySelector('.lightbox-close').addEventListener('click', close);
    lightbox.addEventListener('click', function (e) { if (e.target === lightbox) close(); });

    lightbox.querySelector('.lightbox-prev').addEventListener('click', function (e) {
      e.stopPropagation();
      index = (index - 1 + visible.length) % visible.length;
      render(index);
    });
    lightbox.querySelector('.lightbox-next').addEventListener('click', function (e) {
      e.stopPropagation();
      index = (index + 1) % visible.length;
      render(index);
    });

    document.addEventListener('keydown', function (e) {
      if (!lightbox.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') lightbox.querySelector('.lightbox-prev').click();
      if (e.key === 'ArrowRight') lightbox.querySelector('.lightbox-next').click();
    });
  }

  /* ---- Forms: guard against double-submits ----
     Submission itself is handled by FormSubmit (see the form's action attribute),
     which emails the entry to info@arrow-athletics.com and then redirects to thanks.html */
  document.querySelectorAll('.contact-form').forEach(function (form) {
    form.addEventListener('submit', function () {
      var btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.textContent = 'Sending…';
      }
    });
  });

  /* ---- Footer year ---- */
  var yearEl = document.querySelector('[data-year]');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});
