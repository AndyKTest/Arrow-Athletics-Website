# Arrow Athletics — Arrow Cup Website

The website for **Arrow Cup**, a summer soccer league for girls' and boys' teams. Plain static HTML/CSS/JS — no build step required — hosted on GitHub Pages.

## Pages

- `index.html` — Home
- `about.html` — About the league
- `programs.html` — Girls' and boys' league divisions, format, schedule
- `photos.html` — Photo gallery (filterable, with a lightbox)
- `blog.html` — Blog listing, plus three sample posts:
  `blog-registration-open.html`, `blog-tryout-tips.html`, `blog-meet-the-coaches.html`
- `contact.html` — Contact info + registration form
- `404.html` — Custom not-found page

## Viewing it locally

No build tools needed. From this folder, run a quick local server and open it in a browser:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Publishing with GitHub Pages

1. Push this repo to GitHub (already done if you're reading this from the repo).
2. In the repo, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Choose the `main` branch and the `/ (root)` folder, then save.
5. GitHub will give you a URL like `https://<username>.github.io/Arrow-Athletics-Website/` within a minute or two.

## Things to swap in before launch

- **Photos**: everything in `images/gallery/` and `images/blog/` is a generated placeholder graphic. Replace those files (keep the same filenames, or update the `<img>` paths in the HTML) with real photos whenever you have them.
- **Contact form**: `contact.html` currently points at a placeholder Formspree action (`https://formspree.io/f/your-form-id`). Create a free form at [formspree.io](https://formspree.io) (or any form backend) and swap in your real endpoint — GitHub Pages can't run server-side code, so a form needs an external service to actually receive submissions.
- **Contact info**: the placeholder email (`info@arrowathletics.example`) and phone number in `contact.html` and the footer should be replaced with real details.
- **Social links**: the Instagram/Facebook/X icons in the footer and contact page currently link to `#` — update the `href`s once your accounts exist.
- **Colors/dates**: division dates, season length, and the "Summer 2026" references are placeholders — adjust in the relevant page (or in `dev-tools/build.py`, see below, if you'd rather regenerate).

## Editing the site

You can edit any `.html` file directly — it's plain markup, no templating magic at runtime.

If you'd rather make broader changes (e.g. updating the nav on every page at once, or changing copy across the site), the `dev-tools/` folder has the Python scripts originally used to generate these pages:

- `dev-tools/build.py` — regenerates all HTML pages from shared header/footer/nav templates. Edit the content or templates inside, then run:
  ```bash
  python3 dev-tools/build.py
  ```
  from the repo root (it writes the `.html` files back into the root folder).
- `dev-tools/generate_images.py` — regenerates the placeholder gradient images in `images/`. Not needed once you've swapped in real photos.

Neither script is required for the site to work — they're just a convenience for making sweeping edits later.

## Structure

```
├── index.html, about.html, programs.html, photos.html, blog.html, contact.html, 404.html
├── blog-*.html          # individual blog posts
├── css/style.css        # all site styles
├── js/main.js           # nav toggle, gallery filter + lightbox, form handling
├── images/              # hero, about, gallery, and blog images (placeholders for now)
└── dev-tools/           # optional scripts used to generate the pages/images above
```
