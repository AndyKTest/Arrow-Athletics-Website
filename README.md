# Arrow Athletics — Arrow Cup Website

The website for the **Arrow League** by Arrow Athletics, a summer soccer league for high school boys' and girls' teams across Massachusetts (first season Summer 2027). The **Arrow Cup** is the league's end-of-season knockout tournament. Plain static HTML/CSS/JS — no build step needed to host it — served by GitHub Pages at **arrow-athletics.com**.

## Pages

| File | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About the league |
| `programs.html` | Divisions (boys' and girls' Divisions 1, 2 and 3), season format, what's included, pricing |
| `register.html` | "Interested in Participating?" interest form + FAQ (filename kept so old links still work) |
| `contact.html` | Contact details and general enquiry form |
| `thanks.html` | Confirmation page shown after a form is submitted |
| `photos.html` | Filterable photo gallery with lightbox |
| `blog.html` | News page (currently "Coming Soon") |
| `404.html` | Custom not-found page |

## How the forms work

Both forms (interest form and contact) post to **[FormSubmit](https://formsubmit.co)**, which emails each submission to `info@arrow-athletics.com`. No account, no server, no monthly fee.

**One-time activation:** the first time a form is submitted, FormSubmit emails `info@arrow-athletics.com` asking you to confirm the address. Click the link in that email once and every submission from then on is delivered automatically.

Two things worth knowing:

- The redirect after submitting points at `https://arrow-athletics.com/thanks.html`. If you ever change domains, update the `_next` hidden field in `register.html` and `contact.html` (it's marked with a comment).
- The email address appears in the page source, which spam bots can scrape. If that becomes a problem, FormSubmit gives you a hashed endpoint after activation — swap the `action` URL for that and the address disappears from the HTML.

To switch to a different provider (Formspree, Getform, Web3Forms), just change the `action` attribute on both forms.

## Photos

Every photo on the site is real. `dev-tools/process_photos.py` resized and cropped the original uploads for `gallery-1` … `gallery-12`, `hero.jpg` and `about.jpg`. `gallery-13` … `gallery-18` and the founders' headshots in `images/team/` came from the coaches deck (Nov 2026).

| Files | Used for | Best size |
|---|---|---|
| `images/gallery/gallery-1.jpg` … `gallery-18.jpg` | Photo gallery, home page cards/teaser, division pages, About page | ~1500px on the long side, any aspect ratio (CSS crops to fit) |
| `images/team/andrew.jpg`, `greg.jpg` | Founder headshots on the About page | Portrait, about 3:4 |
| `images/hero.jpg` | Home page hero background | ~2400 × 1230 |
| `images/about.jpg` | About page and home page "our story" image | ~1500 × 1125 |
| `images/merch-jersey.png` | Merch page jersey mock-up | Supplied directly (not generated) — swap the file for a real product photo whenever one exists, same filename |

To add or swap a photo, drop it in `dev-tools/photo_sources/` (or point at it directly), update the filename in the `GALLERY` dict at the top of `dev-tools/process_photos.py`, and re-run:

```bash
python3 dev-tools/process_photos.py
python3 dev-tools/build.py
```

Gallery captions and category tags (Boys / Girls / Matchday / Founders) live in `dev-tools/build.py` (`GALLERY_ITEMS`) — edit the tuple for a given gallery number to retitle or re-tag it. The `photos.html` filter bar only shows a "Championship" button once at least one photo is tagged `championship`.

Free, commercially-usable stock photography if you ever need to fill a gap: [Unsplash](https://unsplash.com), [Pexels](https://pexels.com), [Pixabay](https://pixabay.com).

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

Key values are constants at the top of that file: `LEAGUE_NAME`, `CUP_NAME`, `SEASON`, `STATE`, `PRICE`, `CTA_LABEL` (the "Interested in Participating?" button text), `EMAIL`, `PHONE_DISPLAY`, `DOMAIN`, `FORM_ENDPOINT`. League facts shared by several pages (divisions, season steps, "why choose" reasons, founders) are lists just below the shared templates.

Other scripts in `dev-tools/` (not needed to run the site):

- `process_logo.py` — regenerates the logo variants and favicon from the source artwork
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
