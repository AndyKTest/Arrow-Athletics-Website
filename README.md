# Arrow Athletics — Arrow Cup Website

The website for the **Arrow Cup**, a summer soccer league for high school boys' and girls' teams. Plain static HTML/CSS/JS — no build step needed to host it — served by GitHub Pages at **arrow-athletics.com**.

## Pages

| File | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About the league |
| `programs.html` | Divisions (boys'/girls', varsity/JV) and season format |
| `register.html` | Team registration form + FAQ |
| `contact.html` | Contact details and general enquiry form |
| `thanks.html` | Confirmation page shown after a form is submitted |
| `photos.html` | Filterable photo gallery with lightbox |
| `blog.html` | News index |
| `blog-registration-open.html`, `blog-summer-prep.html`, `blog-coaches-guide.html` | Articles |
| `404.html` | Custom not-found page |

## How the forms work

Both forms (registration and contact) post to **[FormSubmit](https://formsubmit.co)**, which emails each submission to `info@arrow-athletics.com`. No account, no server, no monthly fee.

**One-time activation:** the first time a form is submitted, FormSubmit emails `info@arrow-athletics.com` asking you to confirm the address. Click the link in that email once and every submission from then on is delivered automatically.

Two things worth knowing:

- The redirect after submitting points at `https://arrow-athletics.com/thanks.html`. If you ever change domains, update the `_next` hidden field in `register.html` and `contact.html` (it's marked with a comment).
- The email address appears in the page source, which spam bots can scrape. If that becomes a problem, FormSubmit gives you a hashed endpoint after activation — swap the `action` URL for that and the address disappears from the HTML.

To switch to a different provider (Formspree, Getform, Web3Forms), just change the `action` attribute on both forms.

## Swapping in real photos

Every image in `images/gallery/` and `images/blog/` is a generated brand graphic standing in for real photography. To replace one, **save your photo over the existing file using the same filename** — no code changes needed.

| Files | Used for | Best size |
|---|---|---|
| `images/gallery/gallery-1.jpg` … `gallery-8.jpg` | Photo gallery + home page | 1000 × 750 (4:3) |
| `images/blog/blog-1.jpg` … `blog-3.jpg` | Article headers and cards | 1000 × 560 (16:9) |
| `images/hero.jpg` | Home page hero background | 1920 × 1080 |
| `images/about.jpg` | About page and home page | 1200 × 800 |

Gallery captions live in `dev-tools/build.py` (`GALLERY_ITEMS`) if you want to retitle them.

Free, commercially-usable stock photography: [Unsplash](https://unsplash.com), [Pexels](https://pexels.com), [Pixabay](https://pixabay.com). Search "high school soccer", "youth soccer match", "soccer pitch". All three allow commercial use without attribution — but real photos of your own teams will always beat stock.

## Logo and colours

The palette is taken straight from the logo: navy `#011B46` and electric blue `#0059FC`. Both are defined once at the top of `css/style.css` as CSS variables, so changing them there updates the whole site.

Logo files in `images/`:

- `logo.png` — full colour, for light backgrounds
- `logo-white.png` — white knockout, used in the header and footer
- `mark.png` / `mark-white.png` — arrow mark on its own
- `favicon.png`, `apple-touch-icon.png` — browser tab and phone home-screen icons

## Editing the site

Any `.html` file can be edited directly — it's plain markup.

For changes that affect every page (navigation, footer, contact details, season dates), edit `dev-tools/build.py` instead and re-run it, which regenerates all the HTML from shared templates:

```bash
python3 dev-tools/build.py
```

Key values are constants at the top of that file: `SEASON`, `EMAIL`, `PHONE_DISPLAY`, `DOMAIN`, `FORM_ENDPOINT`.

Other scripts in `dev-tools/` (not needed to run the site):

- `process_logo.py` — regenerates the logo variants and favicon from the source artwork
- `generate_images.py` — regenerates the placeholder brand graphics
- `shot.py` — renders screenshots of every page for review

## Viewing it locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Hosting notes

- `CNAME` (created by GitHub when the custom domain was set) must stay in the repo, or the custom domain stops working.
- `.nojekyll` tells GitHub Pages to serve files as-is rather than running them through Jekyll.
- Fonts (Saira and Inter) load from Google Fonts.

## Structure

```
├── *.html                 # every page
├── css/style.css          # all styling, brand colours defined at the top
├── js/main.js             # mobile nav, gallery filter, lightbox
├── images/                # logo variants, favicon, hero, gallery, blog art
└── dev-tools/             # optional scripts for regenerating pages and assets
```
