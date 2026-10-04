/* ==========================================================================
   Jordan Avery — portfolio microsite
   main.js · vanilla JavaScript, no libraries, ~4 KB unminified.

   Everything in here is an ENHANCEMENT. If this file fails to load, is
   blocked, or JavaScript is switched off entirely, the site still works:
     · the navigation is permanently visible instead of behind a button
     · gallery thumbnails are ordinary links to the full-size images
     · the contact form falls back to the browser's own validation
     · nothing is hidden, because the fade-in styles are scoped to html.js

   CONTENTS
     1  Mobile navigation toggle
     2  Fade-in on scroll (IntersectionObserver)
     3  Gallery lightbox (with keyboard support + focus trap)
     4  Contact form inline validation
     5  Footer year
   ========================================================================== */

(function () {
  'use strict';

  /* Tiny helpers so the code below reads cleanly. */
  var $  = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) {
    return Array.prototype.slice.call((ctx || document).querySelectorAll(sel));
  };


  /* ======================================================================
     1  MOBILE NAVIGATION
     The button is only visible under 680px (see style.css). We keep
     aria-expanded in sync so screen readers announce the state.
     ====================================================================== */
  (function initNav() {
    var toggle = $('.nav-toggle');
    var nav    = $('#primary-nav');
    if (!toggle || !nav) { return; }

    function setOpen(open) {
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      nav.classList.toggle('is-open', open);
    }

    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    /* Close on Escape and hand focus back to the button. */
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });

    /* Close when a link inside the menu is used. */
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { setOpen(false); }
    });

    /* Close when tapping anywhere outside the open menu. */
    document.addEventListener('click', function (e) {
      if (toggle.getAttribute('aria-expanded') !== 'true') { return; }
      if (!nav.contains(e.target) && !toggle.contains(e.target)) { setOpen(false); }
    });

    /* If the window is widened past the breakpoint, drop the open state so
       the desktop layout is never left in a half-open condition. */
    window.addEventListener('resize', function () {
      if (window.innerWidth > 680) { setOpen(false); }
    });
  }());


  /* ======================================================================
     2  FADE-IN ON SCROLL
     Elements with class="reveal" slide up gently the first time they
     appear. We unobserve immediately afterwards so nothing re-animates
     while the visitor scrolls back up.
     ====================================================================== */
  (function initReveal() {
    var items = $$('.reveal');
    if (!items.length) { return; }

    var reduced = window.matchMedia &&
                  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* Old browsers, or someone who asked for less motion: show everything. */
    if (reduced || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }

    var pending = items.slice();          /* everything not yet revealed */

    function reveal(el) {
      el.classList.add('is-in');
      observer.unobserve(el);
      var i = pending.indexOf(el);
      if (i > -1) { pending.splice(i, 1); }
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { reveal(entry.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    items.forEach(function (el) { observer.observe(el); });

    /* Safety net. A very fast scroll (a flick on a phone, a jump to an
       anchor, a restored scroll position) can carry an element from below
       the viewport to above it between two frames. The observer sees no
       intersection either side of that jump and would leave the element
       invisible for good, so we also sweep on scroll: anything whose top
       edge has reached the bottom of the window gets revealed.
       rAF-throttled, and it unbinds itself once the last item is done. */
    function sweep() {
      var h = window.innerHeight;
      pending.slice().forEach(function (el) {
        if (el.getBoundingClientRect().top < h) { reveal(el); }
      });
      if (!pending.length) {
        window.removeEventListener('scroll', onScroll);
        window.removeEventListener('resize', onScroll);
      }
    }

    var ticking = false;
    function onScroll() {
      if (ticking) { return; }
      ticking = true;
      window.requestAnimationFrame(function () { ticking = false; sweep(); });
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    window.setTimeout(sweep, 700);        /* covers a page restored mid-scroll */
  }());


  /* ======================================================================
     3  GALLERY LIGHTBOX
     Thumbnails stay real links (href = the big image), so the gallery
     works without JS. Here we intercept the click and show the overlay.
     ====================================================================== */
  (function initLightbox() {
    var box = $('#lightbox');
    var links = $$('.gallery__link');
    if (!box || !links.length) { return; }

    var img      = $('.lightbox__img', box);
    var caption  = $('.lightbox__caption', box);
    var btnClose = $('.lightbox__close', box);
    var btnPrev  = $('.lightbox__nav--prev', box);
    var btnNext  = $('.lightbox__nav--next', box);
    var index    = 0;
    var lastFocused = null;

    function show(i) {
      index = (i + links.length) % links.length;          /* wrap both ways */
      var link = links[index];
      var thumb = $('.gallery__img', link);

      img.src = link.getAttribute('href');
      /* Reuse the thumbnail's alt text so the big image is described too. */
      img.alt = thumb ? thumb.getAttribute('alt') : '';
      caption.textContent = link.getAttribute('data-caption') || '';
    }

    function open(i) {
      lastFocused = document.activeElement;
      show(i);
      box.hidden = false;
      /* Next frame, so the opacity transition actually runs. */
      window.requestAnimationFrame(function () { box.classList.add('is-visible'); });
      document.body.style.overflow = 'hidden';            /* stop background scroll */
      btnClose.focus();
    }

    function close() {
      box.classList.remove('is-visible');
      document.body.style.overflow = '';
      window.setTimeout(function () { box.hidden = true; img.src = ''; }, 200);
      if (lastFocused) { lastFocused.focus(); }
    }

    links.forEach(function (link, i) {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        open(i);
      });
    });

    btnClose.addEventListener('click', close);
    btnPrev.addEventListener('click', function () { show(index - 1); });
    btnNext.addEventListener('click', function () { show(index + 1); });

    /* Click the dark area (not the image or a button) to dismiss. */
    box.addEventListener('click', function (e) {
      if (e.target === box) { close(); }
    });

    document.addEventListener('keydown', function (e) {
      if (box.hidden) { return; }
      if (e.key === 'Escape')     { close(); }
      if (e.key === 'ArrowLeft')  { show(index - 1); }
      if (e.key === 'ArrowRight') { show(index + 1); }

      /* Keep Tab inside the dialog while it is open. */
      if (e.key === 'Tab') {
        var focusable = [btnClose, btnPrev, btnNext];
        var first = focusable[0];
        var last  = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault(); last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault(); first.focus();
        }
      }
    });
  }());


  /* ======================================================================
     4  CONTACT FORM — friendlier validation
     The HTML deliberately does NOT carry `novalidate`: with JavaScript off
     the browser's own required / type="email" checks still protect the
     form. We add novalidate here, at runtime, so that when this script IS
     running we can show our own calmer messages instead of the browser's.
     ====================================================================== */
  (function initForm() {
    var form = $('#contact-form');
    if (!form) { return; }

    form.noValidate = true;          /* we take over from the browser */

    var status = $('#form-status', form);
    var EMAIL  = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

    var rules = {
      name:    function (v) { return v.trim().length >= 2 ? '' : 'Please tell me your name.'; },
      email:   function (v) { return EMAIL.test(v.trim()) ? '' : 'That email address does not look right.'; },
      message: function (v) { return v.trim().length >= 10 ? '' : 'A sentence or two is plenty — just a little more detail.'; }
    };

    function validateField(field) {
      var rule = rules[field.name];
      if (!rule) { return true; }

      var msg = rule(field.value);
      var out = $('#' + field.id + '-error');

      if (out) { out.textContent = msg; }
      if (msg) {
        field.setAttribute('aria-invalid', 'true');
      } else {
        field.removeAttribute('aria-invalid');
      }
      return !msg;
    }

    /* Validate on blur — never while someone is still typing their first
       character, which is the fastest way to make a form feel hostile. */
    $$('.form__input', form).forEach(function (field) {
      field.addEventListener('blur', function () { validateField(field); });
      field.addEventListener('input', function () {
        if (field.getAttribute('aria-invalid') === 'true') { validateField(field); }
      });
    });

    form.addEventListener('submit', function (e) {
      var fields = $$('.form__input', form);
      var firstBad = null;

      fields.forEach(function (field) {
        if (!validateField(field) && !firstBad) { firstBad = field; }
      });

      if (firstBad) {
        e.preventDefault();
        status.textContent = 'Please check the highlighted fields.';
        firstBad.focus();
        return;
      }

      /* ---- No back end is wired up in this demo. ----------------------
         Point the form's action="" at your handler and DELETE the three
         lines below; the browser will then post the form normally.      */
      e.preventDefault();
      status.textContent = 'Thanks — your message looks good. (Demo form: no address is wired up yet.)';
      form.reset();
    });
  }());


  /* ======================================================================
     5  FOOTER YEAR
     Keeps the copyright line honest without touching the HTML each January.
     The HTML already contains a sensible year, so no-JS visitors see one.
     ====================================================================== */
  (function initYear() {
    $$('#year').forEach(function (el) {
      el.textContent = String(new Date().getFullYear());
    });
  }());

}());
