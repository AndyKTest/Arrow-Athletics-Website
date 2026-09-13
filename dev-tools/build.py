#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds all static HTML pages for the Arrow Cup / Arrow Athletics site
from shared header/footer/lightbox partials, so nav + branding stay in
sync across every page without hand-duplicating markup."""
import os

SITE_NAME = "Arrow Athletics"
CUP_NAME = "Arrow Cup"
YEAR_RANGE = "2026"

ARROW_MARK = """<svg class="brand-mark" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<rect width="48" height="48" rx="12" fill="#F5622E"/>
<path d="M14 30L24 16L34 30" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M24 16V33" stroke="white" stroke-width="4" stroke-linecap="round"/>
</svg>"""

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("programs.html", "Programs"),
    ("photos.html", "Photos"),
    ("blog.html", "Blog"),
    ("contact.html", "Contact"),
]

def head(title, description, active=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | {SITE_NAME}</title>
<meta name="description" content="{description}">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<meta property="og:title" content="{title} | {SITE_NAME}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
</head>
<body>
"""

def header(active):
    links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ""
        links.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    links_html = "\n        ".join(links)
    return f"""<header class="site-header">
  <div class="nav-wrap">
    <a href="index.html" class="brand">
      {ARROW_MARK}
      <span>{SITE_NAME.upper()}<small>{CUP_NAME} &middot; Summer Soccer League</small></span>
    </a>
    <ul class="nav-links">
        {links_html}
        <li class="nav-cta"><a href="contact.html" class="btn btn-primary btn-sm">Register Interest</a></li>
    </ul>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
"""

def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          {ARROW_MARK}
          <span>{SITE_NAME.upper()}</span>
        </div>
        <p>{CUP_NAME} is a summer soccer league for girls and boys, built around real competition, real community, and a championship weekend every team remembers. More sports joining in future seasons.</p>
        <div class="social-row">
          <a href="#" aria-label="Instagram" title="Instagram">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.8"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>
          </a>
          <a href="#" aria-label="Facebook" title="Facebook">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M15 8.5h2V5h-2c-2.2 0-4 1.8-4 4v2H9v3.5h2V21h3.5v-6.5H17l.5-3.5h-3V9c0-.6.4-1 1-1z" fill="currentColor"/></svg>
          </a>
          <a href="#" aria-label="X / Twitter" title="X / Twitter">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M4 4l16 16M20 4L4 20" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="about.html">About the League</a></li>
          <li><a href="programs.html">Girls &amp; Boys Programs</a></li>
          <li><a href="photos.html">Photo Gallery</a></li>
          <li><a href="blog.html">Blog &amp; News</a></li>
        </ul>
      </div>
      <div>
        <h4>Get Involved</h4>
        <ul>
          <li><a href="contact.html">Register a Team</a></li>
          <li><a href="contact.html">Volunteer / Coach</a></li>
          <li><a href="contact.html">Sponsor the Cup</a></li>
          <li><a href="contact.html">General Questions</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:info@arrowathletics.example">info@arrowathletics.example</a></li>
          <li><span>Summer League &middot; {YEAR_RANGE}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>{YEAR_RANGE}</span> {SITE_NAME}. All rights reserved.</span>
      <span>Built for the {CUP_NAME} summer soccer league.</span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""

def lightbox():
    return """<div class="lightbox">
  <button class="lightbox-close" aria-label="Close">&times;</button>
  <button class="lightbox-nav lightbox-prev" aria-label="Previous">&#8249;</button>
  <img src="" alt="">
  <button class="lightbox-nav lightbox-next" aria-label="Next">&#8250;</button>
</div>
"""

def write(path, html):
    with open(path, "w") as f:
        f.write(html)
    print("wrote", path)

# Convenience icon set (feature icons)
ICON = {
    "trophy": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M7 4h10v4a5 5 0 01-10 0V4z" stroke="currentColor" stroke-width="1.8"/><path d="M7 5H4v2a3 3 0 003 3M17 5h3v2a3 3 0 01-3 3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M10 13v2a2 2 0 002 2 2 2 0 002-2v-2M9 20h6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "users": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="9" cy="8" r="3" stroke="currentColor" stroke-width="1.8"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="17" cy="8" r="2.4" stroke="currentColor" stroke-width="1.6"/><path d="M15.5 14.3c2.6.4 4.5 2.7 4.5 5.7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "heart": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 20s-7-4.4-9.5-8.8C.7 8 2.4 4.8 5.8 4.2c2-.3 3.7.6 4.9 2.2 1.2-1.6 2.9-2.5 4.9-2.2 3.4.6 5.1 3.8 3.3 7C19 15.6 12 20 12 20z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "ball": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M12 8l3.5 2.5-1.3 4h-4.4L8.5 10.5 12 8z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M12 3v5M3.5 9l4.5 1M20.5 9l-4.5 1M6 20l2-4.5M18 20l-2-4.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>',
    "calendar": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="16" rx="2" stroke="currentColor" stroke-width="1.7"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "shield": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "pin": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 21s7-6.6 7-11.5a7 7 0 10-14 0C5 14.4 12 21 12 21z" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="9.5" r="2.4" stroke="currentColor" stroke-width="1.6"/></svg>',
    "mail": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2" stroke="currentColor" stroke-width="1.7"/><path d="M4 6.5l8 6 8-6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "phone": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M6 3h3l1.5 4-2 1.5a12 12 0 006 6l1.5-2 4 1.5v3a2 2 0 01-2.2 2A17 17 0 014 5.2 2 2 0 016 3z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "clock": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M12 7v5l3.5 2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
}

os.makedirs("images", exist_ok=True)

# =========================================================
# HOME
# =========================================================
def page_home():
    html = head(
        "Home",
        "Arrow Cup is a summer soccer league for girls and boys, built around real competition, community, and a championship weekend."
    )
    html += header("index.html")
    html += f"""
<section class="hero">
  <div class="hero-bg" style="background-image:url('images/hero.jpg')"></div>
  <div class="hero-overlay"></div>
  <div class="hero-inner">
    <div class="eyebrow" style="color:#ff8a4c">Summer {YEAR_RANGE} &middot; Girls &amp; Boys Soccer</div>
    <h1>A summer soccer league worth showing up for.</h1>
    <p class="lede">{CUP_NAME} brings girls' and boys' teams together for a full summer season of league play, capped off with a championship weekend nobody forgets. Built by people who love this sport.</p>
    <div class="hero-actions">
      <a href="contact.html" class="btn btn-primary">Register Your Team</a>
      <a href="programs.html" class="btn btn-outline">View Programs</a>
    </div>
    <div class="stat-strip">
      <div class="stat-item"><strong>2</strong><span>Leagues &mdash; Girls &amp; Boys</span></div>
      <div class="stat-item"><strong>Ages 8&ndash;18</strong><span>Divisions for every age</span></div>
      <div class="stat-item"><strong>10</strong><span>Weeks of summer play</span></div>
      <div class="stat-item"><strong>1</strong><span>Championship Weekend</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid grid-2" style="align-items:center; gap:56px;">
      <div>
        <div class="eyebrow">What is {CUP_NAME}?</div>
        <h2>A new summer tradition, built one season at a time.</h2>
        <p>{CUP_NAME} started with a simple idea: give girls' and boys' soccer players a competitive, well-run summer league where the games matter, the coaching is real, and every team gets a shot at the title. This year it's soccer. Down the road, we're planning to bring in more sports &mdash; lacrosse and beyond.</p>
        <p>Whether your player is lacing up for their first season or chasing a championship, {CUP_NAME} is built to be the highlight of their summer.</p>
        <a href="about.html" class="btn btn-navy">Learn Our Story</a>
      </div>
      <div>
        <img src="images/about.jpg" alt="Arrow Cup summer soccer league" style="border-radius:20px; box-shadow:var(--shadow-lg);">
      </div>
    </div>
  </div>
</section>

<section style="background:#fff;">
  <div class="container">
    <div class="center" style="margin-bottom:44px;">
      <div class="eyebrow">Programs</div>
      <h2>Two leagues. One summer. All heart.</h2>
      <p class="lede mx-auto">Separate divisions for girls and boys, grouped by age, so every player competes at the right level.</p>
    </div>
    <div class="grid grid-2">
      <div class="card">
        <div class="card-media"><img src="images/gallery/gallery-2.jpg" alt="Girls soccer league"><span class="tag tag-girls">Girls League</span></div>
        <div class="card-body">
          <h3>Girls Soccer League</h3>
          <p>Competitive divisions for ages 8&ndash;18, with a full regular season and a championship bracket every August.</p>
          <a href="programs.html#girls">See divisions &amp; dates &rarr;</a>
        </div>
      </div>
      <div class="card">
        <div class="card-media"><img src="images/gallery/gallery-6.jpg" alt="Boys soccer league"><span class="tag tag-boys">Boys League</span></div>
        <div class="card-body">
          <h3>Boys Soccer League</h3>
          <p>The same summer-long format for boys' teams &mdash; age-grouped play, real refs, and a title on the line.</p>
          <a href="programs.html#boys">See divisions &amp; dates &rarr;</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="center" style="margin-bottom:44px;">
      <div class="eyebrow">From the Blog</div>
      <h2>News &amp; updates</h2>
    </div>
    <div class="grid grid-3">
      {blog_card("blog-registration-open.html", "images/blog/blog-1.jpg", "news", "News", "Registration Is Open", "Girls' and boys' divisions are open for the " + YEAR_RANGE + " season. Here's what to know before you sign up.")}
      {blog_card("blog-tryout-tips.html", "images/blog/blog-2.jpg", "tips", "Tips", "5 Tips Before Tryouts", "Simple, practical advice to help new players walk into tryouts feeling ready and confident.")}
      {blog_card("blog-meet-the-coaches.html", "images/blog/blog-3.jpg", "community", "Community", "Meet the Coaches", "A look at the coaching staff building out the first {CUP_NAME} season, and what they're focused on.".format(CUP_NAME=CUP_NAME))}
    </div>
    <div class="center" style="margin-top:36px;"><a href="blog.html" class="btn btn-navy">Read the Blog</a></div>
  </div>
</section>

<section style="background:#fff;">
  <div class="container">
    <div class="center" style="margin-bottom:36px;">
      <div class="eyebrow">Gallery</div>
      <h2>Moments from the pitch</h2>
    </div>
    <div class="grid grid-4" style="gap:16px;">
      {"".join(home_gallery_thumb(n) for n in [1,3,5,7])}
    </div>
    <div class="center" style="margin-top:32px;"><a href="photos.html" class="btn btn-navy">View Full Gallery</a></div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-banner">
      <h2>Ready to join {CUP_NAME}?</h2>
      <p class="lede mx-auto">Registration is open for girls' and boys' divisions this summer. Spots fill up by division, so don't wait too long.</p>
      <a href="contact.html" class="btn btn-navy" style="margin-top:10px;">Register Your Team</a>
    </div>
  </div>
</section>
"""
    html += footer()
    return html

def blog_card(href, img, cat, tag_label, title, excerpt):
    return f"""<div class="card">
        <div class="card-media"><img src="{img}" alt="{title}"><span class="tag tag-{cat}">{tag_label}</span></div>
        <div class="card-body">
          <h3>{title}</h3>
          <p>{excerpt}</p>
          <a href="{href}">Read more &rarr;</a>
        </div>
      </div>"""

def home_gallery_thumb(n):
    return f'<a href="photos.html" class="gallery-item"><img src="images/gallery/gallery-{n}.jpg" alt="Arrow Cup photo {n}"></a>'

write("index.html", page_home())

# =========================================================
# ABOUT
# =========================================================
def page_about():
    html = head(
        "About",
        f"About {CUP_NAME} — a summer soccer league for girls and boys built on community, competition, and character."
    )
    html += header("about.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb">About Us</div>
    <h1>Built for the love of the game.</h1>
    <p>{CUP_NAME} is a summer soccer league for girls and boys &mdash; and the beginning of something bigger.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid grid-2" style="align-items:center; gap:56px;">
      <div>
        <img src="images/about.jpg" alt="Arrow Athletics story" style="border-radius:20px; box-shadow:var(--shadow-lg);">
      </div>
      <div>
        <div class="eyebrow">Our Story</div>
        <h2>Why we started {CUP_NAME}</h2>
        <p>{SITE_NAME} started with a straightforward goal: build a summer league that takes youth soccer seriously without losing the fun of it. That means real schedules, real officiating, and a championship weekend worth training for &mdash; for girls' and boys' teams alike.</p>
        <p>This first season, we're focused entirely on soccer. As {CUP_NAME} grows, the plan is to expand into more sports &mdash; lacrosse is next on the list &mdash; so the league can grow with the athletes in it.</p>
      </div>
    </div>
  </div>
</section>

<section style="background:#fff;">
  <div class="container">
    <div class="center" style="margin-bottom:44px;">
      <div class="eyebrow">What We're About</div>
      <h2>The values behind the league</h2>
    </div>
    <div class="grid grid-4">
      <div class="feature">
        <div class="feature-icon">{ICON['users']}</div>
        <div><h3>Community</h3><p>Families, coaches, and players building something together every summer.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['trophy']}</div>
        <div><h3>Real Competition</h3><p>A genuine season and playoff bracket &mdash; not just a weekend jamboree.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['heart']}</div>
        <div><h3>Character</h3><p>Sportsmanship and effort matter here as much as the final score.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['ball']}</div>
        <div><h3>Growth</h3><p>Soccer first &mdash; with more sports on the way as the league grows.</p></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-banner">
      <h2>Want to get involved?</h2>
      <p class="lede mx-auto">Whether you're registering a team, looking to coach, or just have questions &mdash; we'd love to hear from you.</p>
      <a href="contact.html" class="btn btn-navy" style="margin-top:10px;">Get In Touch</a>
    </div>
  </div>
</section>
"""
    html += footer()
    return html

write("about.html", page_about())

print("Home + About built.")

# =========================================================
# PROGRAMS
# =========================================================
def age_rows(rows):
    trs = "\n".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
    return f"""<table class="age-table">
          <thead><tr><th>Division</th><th>Ages</th><th>Format</th></tr></thead>
          <tbody>{trs}</tbody>
        </table>"""

def page_programs():
    html = head(
        "Programs",
        f"{CUP_NAME} programs: girls' and boys' summer soccer divisions by age group, season format, and championship weekend."
    )
    html += header("programs.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb">Programs</div>
    <h1>Girls &amp; Boys Summer Soccer</h1>
    <p>Age-grouped divisions, a full summer season, and a championship weekend to close it out. More sports are on the way in future seasons &mdash; this year, it's all soccer.</p>
  </div>
</section>

<section>
  <div class="container">
    <div id="girls" class="league-block girls">
      <div class="league-head">
        <div>
          <span class="tag tag-girls">Girls League</span>
          <h2 class="mt-0" style="margin-top:12px;">Girls Soccer League</h2>
        </div>
        <a href="contact.html" class="btn btn-primary btn-sm">Register a Girls' Team</a>
      </div>
      <p>Competitive, well-coached play across five age divisions. Every team gets a full regular season plus a spot in the end-of-summer bracket.</p>
      {age_rows([
          ("U8", "8 &amp; under", "Small-sided, 7v7"),
          ("U10", "9&ndash;10", "7v7 league play"),
          ("U12", "11&ndash;12", "9v9 league play"),
          ("U14", "13&ndash;14", "11v11 league play"),
          ("U16/U18", "15&ndash;18", "11v11 league play"),
      ])}
    </div>

    <div id="boys" class="league-block boys">
      <div class="league-head">
        <div>
          <span class="tag tag-boys">Boys League</span>
          <h2 class="mt-0" style="margin-top:12px;">Boys Soccer League</h2>
        </div>
        <a href="contact.html" class="btn btn-primary btn-sm">Register a Boys' Team</a>
      </div>
      <p>The same summer-long structure for boys' teams &mdash; balanced divisions, consistent officiating, and a championship weekend to play for.</p>
      {age_rows([
          ("U8", "8 &amp; under", "Small-sided, 7v7"),
          ("U10", "9&ndash;10", "7v7 league play"),
          ("U12", "11&ndash;12", "9v9 league play"),
          ("U14", "13&ndash;14", "11v11 league play"),
          ("U16/U18", "15&ndash;18", "11v11 league play"),
      ])}
    </div>
  </div>
</section>

<section style="background:#fff;">
  <div class="container">
    <div class="center" style="margin-bottom:44px;">
      <div class="eyebrow">Season Format</div>
      <h2>How the summer works</h2>
    </div>
    <div class="grid grid-3">
      <div class="feature">
        <div class="feature-icon">{ICON['calendar']}</div>
        <div><h3>Regular Season</h3><p>Weekly games across a 10-week summer schedule, organized by division.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['shield']}</div>
        <div><h3>Officiated Play</h3><p>Every match is refereed, scored, and tracked in the standings.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['trophy']}</div>
        <div><h3>{CUP_NAME} Championship</h3><p>The season closes with a championship weekend for every division.</p></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-banner">
      <h2>Registration is open for {YEAR_RANGE}</h2>
      <p class="lede mx-auto">Reach out to register a team, ask about a division, or find out how to get a new team started.</p>
      <a href="contact.html" class="btn btn-navy" style="margin-top:10px;">Register Now</a>
    </div>
  </div>
</section>
"""
    html += footer()
    return html

write("programs.html", page_programs())

# =========================================================
# PHOTOS
# =========================================================
GALLERY_ITEMS = [
    (1, "all",  "cup",      "cup",       "Arrow Cup Kickoff Weekend"),
    (2, "girls","girls",    "girls",     "Girls U14 Final &mdash; Championship Saturday"),
    (3, "boys", "boys",     "boys",      "Boys U12 Match Day &mdash; Group Stage"),
    (4, "training","training","training","Summer Skills Clinic"),
    (5, "girls","girls",    "girls",     "Girls U16 Semifinal, Under the Lights"),
    (6, "boys", "boys",     "boys",      "Boys U10 Kickoff &mdash; First Goals"),
    (7, "all",  "cup",      "cup",       "Team Huddle Before Kickoff"),
    (8, "all",  "cup",      "cup",       "Trophy Presentation &mdash; Closing Ceremony"),
]

def gallery_item(n, category, tagcls, tagtxt, caption):
    label = {"girls": "Girls", "boys": "Boys", "training": "Training", "cup": "Arrow Cup"}[tagtxt]
    return f"""<div class="gallery-item" data-category="{category}">
      <img src="images/gallery/gallery-{n}.jpg" alt="{caption}">
      <span class="tag tag-{tagcls}" style="position:absolute; top:14px; left:14px;">{label}</span>
      <div class="gallery-cap">{caption}</div>
    </div>"""

def page_photos():
    html = head(
        "Photo Gallery",
        f"Photos from {CUP_NAME} &mdash; girls' and boys' league games, training, and championship weekend."
    )
    html += header("photos.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb">Gallery</div>
    <h1>Moments from the Pitch</h1>
    <p>Game days, training sessions, and championship weekend &mdash; captured across the {CUP_NAME} season.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="filter-bar">
      <button class="filter-btn active" data-filter="all">All Photos</button>
      <button class="filter-btn" data-filter="girls">Girls League</button>
      <button class="filter-btn" data-filter="boys">Boys League</button>
      <button class="filter-btn" data-filter="training">Training</button>
    </div>
    <div class="gallery-grid">
      {"".join(gallery_item(*item) for item in GALLERY_ITEMS)}
    </div>
    <p class="center" style="margin-top:32px; font-size:0.9rem;">Placeholder images shown above &mdash; swap in real photos any time by replacing the files in <code>images/gallery/</code>.</p>
  </div>
</section>
{lightbox()}
"""
    html += footer()
    return html

write("photos.html", page_photos())
print("Programs + Photos built.")

# =========================================================
# BLOG (listing)
# =========================================================
BLOG_POSTS = [
    {
        "slug": "blog-registration-open.html",
        "img": "images/blog/blog-1.jpg",
        "cat": "news", "tag": "News",
        "title": "Registration Is Open for the {} Season".format(YEAR_RANGE),
        "date": "June 1, " + YEAR_RANGE,
        "excerpt": "Girls' and boys' divisions are open for registration. Here's what to know about age groups, dates, and how to get a team signed up.",
    },
    {
        "slug": "blog-tryout-tips.html",
        "img": "images/blog/blog-2.jpg",
        "cat": "tips", "tag": "Tips",
        "title": "5 Tips Before Tryouts",
        "date": "June 8, " + YEAR_RANGE,
        "excerpt": "Simple, practical advice for new players &mdash; girls and boys, any division &mdash; walking into tryouts for the first time.",
    },
    {
        "slug": "blog-meet-the-coaches.html",
        "img": "images/blog/blog-3.jpg",
        "cat": "community", "tag": "Community",
        "title": "Meet the Coaches Building This Season",
        "date": "June 15, " + YEAR_RANGE,
        "excerpt": "A look at the coaching staff behind the first {} season, and what they're focused on building.".format(CUP_NAME),
    },
]

def page_blog():
    html = head("Blog", f"News and updates from {CUP_NAME} &mdash; registration, tips, and league updates.")
    html += header("blog.html")
    cards = "".join(
        blog_card(p["slug"], p["img"], p["cat"], p["tag"], p["title"], p["excerpt"]) for p in BLOG_POSTS
    )
    html += f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb">Blog</div>
    <h1>News &amp; Updates</h1>
    <p>What's happening around {CUP_NAME} &mdash; registration news, player tips, and league updates.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid grid-3">
      {cards}
    </div>
  </div>
</section>
"""
    html += footer()
    return html

write("blog.html", page_blog())

# =========================================================
# BLOG POST TEMPLATE
# =========================================================
def article(slug, img, cat, tag, title, date, body_paragraphs):
    html = head(title, f"{title} &mdash; {CUP_NAME} blog.")
    html += header("blog.html")
    body_html = "\n".join(
        f"<h2>{p[1]}</h2>" if p[0] == "h2" else f"<p>{p[1]}</p>" if p[0] == "p" else
        ("<ul>" + "".join(f"<li>{li}</li>" for li in p[1]) + "</ul>")
        for p in body_paragraphs
    )
    html += f"""
<section class="article-hero">
  <div class="container">
    <a href="blog.html" class="back-link" style="color:rgba(255,255,255,0.75)">&larr; Back to Blog</a>
    <span class="tag tag-{cat}">{tag}</span>
    <h1 style="margin-top:14px;">{title}</h1>
    <div class="article-meta">{date}</div>
  </div>
  <div class="article-cover"><img src="{img}" alt="{title}"></div>
</section>
<section>
  <div class="container">
    <div class="article-body">
      {body_html}
    </div>
  </div>
</section>
"""
    html += footer()
    write(slug, html)

article(
    "blog-registration-open.html",
    "images/blog/blog-1.jpg", "news", "News",
    f"Registration Is Open for the {YEAR_RANGE} Season",
    f"June 1, {YEAR_RANGE}",
    [
        ("p", f"Registration for the {YEAR_RANGE} {CUP_NAME} season is officially open, with divisions available for both girls' and boys' teams across all age groups."),
        ("h2", "What's included this season"),
        ("p", "Every registered team gets a full 10-week regular season, officiated matches, tracked standings, and a guaranteed spot in the end-of-summer championship bracket."),
        ("ul", [
            "Girls' and boys' divisions from U8 through U18",
            "Weekly league games across the summer",
            "A championship weekend to close out the season",
        ]),
        ("h2", "How to register"),
        ("p", "Head over to the Contact page and let us know your player's or team's age group. We'll follow up with next steps, key dates, and everything you need before the season kicks off."),
        ("p", "Spots are limited by division, so teams that register early get first pick of game-day scheduling."),
    ],
)

article(
    "blog-tryout-tips.html",
    "images/blog/blog-2.jpg", "tips", "Tips",
    "5 Tips Before Tryouts",
    f"June 8, {YEAR_RANGE}",
    [
        ("p", "Tryouts can be nerve-wracking, especially for players stepping onto a new team for the first time. Here are five simple things that make a real difference &mdash; for girls' and boys' divisions alike."),
        ("h2", "1. Show up early and warmed up"),
        ("p", "Arriving with time to stretch and touch the ball before evaluations start helps players settle in and play like themselves."),
        ("h2", "2. Hydrate the day before, not just the day of"),
        ("p", "Summer heat is real. Good hydration starts 24 hours ahead, not five minutes before kickoff."),
        ("h2", "3. Focus on effort, not perfection"),
        ("p", "Coaches are watching hustle, communication, and coachability at least as much as raw skill."),
        ("h2", "4. Communicate on the field"),
        ("p", "Calling for the ball, talking to teammates, and staying vocal on defense stands out immediately."),
        ("h2", "5. Ask questions afterward"),
        ("p", "Players who ask coaches what to work on show they're serious about improving &mdash; and coaches remember that."),
    ],
)

article(
    "blog-meet-the-coaches.html",
    "images/blog/blog-3.jpg", "community", "Community",
    "Meet the Coaches Building This Season",
    f"June 15, {YEAR_RANGE}",
    [
        ("p", f"Every good league starts with good coaching, and that's exactly where we've focused our energy building the first {CUP_NAME} season."),
        ("h2", "What we look for in a coach"),
        ("p", "Experience matters, but so does temperament. We're building a staff around coaches who take the game seriously and take their players even more seriously."),
        ("ul", [
            "Real coaching or playing experience in youth soccer",
            "A track record of positive, development-focused coaching",
            "Genuine investment in both the girls' and boys' divisions",
        ]),
        ("h2", "Coaching openings"),
        ("p", "We're still building out staff for several divisions this season. If you're interested in coaching &mdash; for either the girls' or boys' league &mdash; reach out through the Contact page. We'd love to talk."),
    ],
)

print("Blog built.")

# =========================================================
# CONTACT
# =========================================================
def page_contact():
    html = head(
        "Contact",
        f"Get in touch with {CUP_NAME} &mdash; register a team, ask about coaching, or send a general question."
    )
    html += header("contact.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb">Contact</div>
    <h1>Let's Talk {CUP_NAME}</h1>
    <p>Registering a team, coaching, sponsoring, or just have a question? Reach out below.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid grid-2" style="align-items:flex-start; gap:40px;">
      <div class="contact-info-card">
        <h3>Contact Info</h3>
        <div class="contact-row">
          <span class="ic">{ICON['mail']}</span>
          <div><strong>Email</strong><a href="mailto:info@arrowathletics.example">info@arrowathletics.example</a></div>
        </div>
        <div class="contact-row">
          <span class="ic">{ICON['phone']}</span>
          <div><strong>Phone</strong><span>(555) 010-0100</span></div>
        </div>
        <div class="contact-row">
          <span class="ic">{ICON['pin']}</span>
          <div><strong>Location</strong><span>Fields &amp; league office address coming soon</span></div>
        </div>
        <div class="contact-row">
          <span class="ic">{ICON['clock']}</span>
          <div><strong>Season</strong><span>Summer {YEAR_RANGE} &middot; Registration open now</span></div>
        </div>
        <div class="social-row">
          <a href="#" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.8"/></svg></a>
          <a href="#" aria-label="Facebook"><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M15 8.5h2V5h-2c-2.2 0-4 1.8-4 4v2H9v3.5h2V21h3.5v-6.5H17l.5-3.5h-3V9c0-.6.4-1 1-1z" fill="currentColor"/></svg></a>
        </div>
      </div>

      <div>
        <h3>Send a Message</h3>
        <p class="form-note" style="margin-bottom:18px;">This form isn't wired to an inbox yet &mdash; connect it to a form backend such as Formspree, then update the <code>action</code> attribute in <code>contact.html</code>. Until then, please use the email above.</p>
        <form class="contact-form" action="https://formspree.io/f/your-form-id" method="POST">
          <div class="form-grid">
            <div>
              <label for="name">Full Name</label>
              <input id="name" name="name" type="text" required>
            </div>
            <div>
              <label for="email">Email</label>
              <input id="email" name="email" type="email" required>
            </div>
            <div>
              <label for="role">I am a...</label>
              <select id="role" name="role">
                <option>Parent / Guardian</option>
                <option>Player</option>
                <option>Coach</option>
                <option>Sponsor</option>
                <option>Other</option>
              </select>
            </div>
            <div>
              <label for="division">Division of Interest</label>
              <select id="division" name="division">
                <option>Girls League</option>
                <option>Boys League</option>
                <option>Not Sure Yet</option>
              </select>
            </div>
            <div class="full">
              <label for="message">Message</label>
              <textarea id="message" name="message" required placeholder="Tell us a bit about your player, team, or question..."></textarea>
            </div>
            <div class="full">
              <button type="submit" class="btn btn-primary">Send Message</button>
              <div class="form-success">Thanks for reaching out! We'll get back to you shortly.</div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>
"""
    html += footer()
    return html

write("contact.html", page_contact())

# =========================================================
# 404
# =========================================================
def page_404():
    html = head("Page Not Found", f"This page moved or doesn't exist &mdash; head back to {CUP_NAME}.")
    html += header("")
    html += f"""
<section class="page-hero" style="padding-top:110px; padding-bottom:100px;">
  <div class="container">
    <div class="eyebrow" style="color:#ff8a4c;">404</div>
    <h1>Offside &mdash; this page doesn't exist.</h1>
    <p>The page you're looking for was moved, renamed, or never existed. Let's get you back on the pitch.</p>
    <div style="margin-top:24px;"><a href="index.html" class="btn btn-primary">Back to Home</a></div>
  </div>
</section>
"""
    html += footer()
    return html

write("404.html", page_404())

print("Contact + 404 built. All pages generated.")
