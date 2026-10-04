# Responsive portfolio microsite

A three-page portfolio site built by hand in plain HTML5, CSS3 and vanilla
JavaScript. No frameworks, no build step, no third-party requests — open
`index.html` in a browser and it runs.

**Live demo:** https://anirudhatalmale6-alt.github.io/portfolio-microsite-demo/

> The name, copy and artwork are placeholders so the layout can be seen
> working. They're meant to be replaced — [GUIDE.md](GUIDE.md) explains how.

---

## Pages

| File | What it is |
|---|---|
| `index.html` | Home — hero, three featured projects, about, call to action |
| `work.html` | Gallery of six projects with a keyboard-accessible lightbox |
| `contact.html` | Contact form with inline validation, plus studio details |

## How it's put together

```
index.html  work.html  contact.html
css/style.css      one stylesheet, commented, 12 numbered sections
js/main.js         one script, commented, 5 numbered sections, ~5 KB
images/            6 project SVGs, portrait, favicon, social card
GUIDE.md / .pdf    plain-language editing and upload guide
tools/             the script that generated the placeholder artwork
```

Total page weight is around 100 KB including every image, because the
artwork is SVG and the type is a system font stack — there are no font
downloads and nothing is fetched from a CDN.

## What it does

- **Responsive** without breakpoint soup: `clamp()` for fluid type and
  `grid-template-columns: repeat(auto-fit, minmax(…, 1fr))` for the card and
  gallery grids, so they reflow at any width rather than at three fixed sizes.
- **Works without JavaScript.** The inline `html.js` flag means the fade-in
  styles only apply when the script is running. With JS off the navigation is
  permanently visible, the gallery thumbnails are ordinary links to the
  full-size images, and the form falls back to the browser's own validation.
  Nothing is hidden and nothing is dead.
- **Accessible.** Skip link, semantic landmarks, visible focus rings, an
  `aria-expanded` menu button, a lightbox with `aria-modal`, Escape-to-close,
  arrow-key navigation and a focus trap that returns focus where it came
  from. Every colour pairing measures 5.7:1 or better against WCAG AA.
- **SEO basics.** Per-page title, description and keywords, a canonical link,
  Open Graph tags, one `<h1>` per page, a sensible heading order and a real
  description in every `alt`.
- **Respects the visitor.** Honours `prefers-reduced-motion` and
  `prefers-color-scheme`, and prints cleanly with the chrome stripped out.

## Tested

Chromium, Gecko (Firefox) and WebKit (Safari) via Playwright, at 1280px,
834px and 390px, plus a pass with JavaScript disabled and a pass in dark
mode. Checked for console errors, horizontal overflow and unrevealed
content after a fast scroll.

## Editing it

See **[GUIDE.md](GUIDE.md)** — or `GUIDE.pdf` for the same thing in print.
It covers changing text, swapping images, re-colouring, wiring the contact
form to a real inbox, and three ways to put the site online.

## Licence

MIT — use it, change it, ship it.
