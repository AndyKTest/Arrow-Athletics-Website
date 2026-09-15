#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds every static HTML page for the Arrow Athletics / Arrow Cup site from
shared partials, so the nav, branding and footer stay identical across pages.

Run from the repo root:   python3 dev-tools/build.py
"""
import os

SITE_NAME = "Arrow Athletics"
CUP_NAME = "Arrow Cup"
SEASON = "Summer 2026"
YEAR = "2026"
EMAIL = "info@arrow-athletics.com"
PHONE_DISPLAY = "+1 (774) 270-9555"
PHONE_LINK = "+17742709555"
DOMAIN = "https://arrow-athletics.com"

# Where registration + contact submissions are emailed.
# FormSubmit relays the submission straight to the address below — no account needed.
FORM_ENDPOINT = f"https://formsubmit.co/{EMAIL}"

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("programs.html", "Divisions"),
    ("photos.html", "Photos"),
    ("blog.html", "News"),
    ("contact.html", "Contact"),
]


def head(title, description, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | {SITE_NAME}</title>
<meta name="description" content="{description}">
<link rel="icon" href="images/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Saira:ital,wght@0,500;0,600;0,700;0,800;1,700;1,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<meta property="og:title" content="{title} | {SITE_NAME}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{DOMAIN}/images/logo.png">
<meta property="og:type" content="website">
<meta name="theme-color" content="#011B46">
{extra}</head>
<body>
"""


def header(active):
    links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ""
        links.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    links_html = "\n        ".join(links)
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="nav-wrap">
    <a href="index.html" class="brand" aria-label="{SITE_NAME} home">
      <img src="images/logo-white.png" alt="{SITE_NAME}" class="brand-logo">
    </a>
    <nav>
      <ul class="nav-links">
        {links_html}
        <li class="nav-cta"><a href="register.html" class="btn btn-primary btn-sm">Register a Team</a></li>
      </ul>
    </nav>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<main id="main">
"""


def footer():
    return f"""</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img src="images/logo-white.png" alt="{SITE_NAME}" class="footer-logo">
        <p>{CUP_NAME} is a {SEASON.lower()} soccer league for high school boys' and girls' teams &mdash; real divisions, real officiating, and a championship weekend to finish the summer.</p>
        <div class="social-row">
          <a href="#" aria-label="Instagram" title="Instagram">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.8"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>
          </a>
          <a href="#" aria-label="Facebook" title="Facebook">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M15 8.5h2V5h-2c-2.2 0-4 1.8-4 4v2H9v3.5h2V21h3.5v-6.5H17l.5-3.5h-3V9c0-.6.4-1 1-1z" fill="currentColor"/></svg>
          </a>
          <a href="mailto:{EMAIL}" aria-label="Email us" title="Email us">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2" stroke="currentColor" stroke-width="1.7"/><path d="M4 6.5l8 6 8-6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          </a>
        </div>
      </div>
      <div>
        <h4>League</h4>
        <ul>
          <li><a href="about.html">About the League</a></li>
          <li><a href="programs.html">Divisions &amp; Format</a></li>
          <li><a href="photos.html">Photo Gallery</a></li>
          <li><a href="blog.html">News &amp; Updates</a></li>
        </ul>
      </div>
      <div>
        <h4>Get Involved</h4>
        <ul>
          <li><a href="register.html">Register a Team</a></li>
          <li><a href="contact.html">Coach &amp; Referee Inquiries</a></li>
          <li><a href="contact.html">Sponsor the Cup</a></li>
          <li><a href="contact.html">General Questions</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a></li>
          <li><span>{SEASON} &middot; Registration open</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>{YEAR}</span> {SITE_NAME}. All rights reserved.</span>
      <span>High school boys' &amp; girls' summer soccer.</span>
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


ICON = {
    "trophy": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M7 4h10v4a5 5 0 01-10 0V4z" stroke="currentColor" stroke-width="1.8"/><path d="M7 5H4v2a3 3 0 003 3M17 5h3v2a3 3 0 01-3 3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M10 13v2a2 2 0 002 2 2 2 0 002-2v-2M9 20h6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "users": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="9" cy="8" r="3" stroke="currentColor" stroke-width="1.8"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="17" cy="8" r="2.4" stroke="currentColor" stroke-width="1.6"/><path d="M15.5 14.3c2.6.4 4.5 2.7 4.5 5.7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "whistle": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M3 11a5 5 0 015-5h8l5-2v6.5A6.5 6.5 0 0112.5 17H8a5 5 0 01-5-5z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="8.5" cy="11.5" r="2" stroke="currentColor" stroke-width="1.6"/></svg>',
    "ball": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M12 8l3.5 2.5-1.3 4h-4.4L8.5 10.5 12 8z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M12 3v5M3.5 9l4.5 1M20.5 9l-4.5 1M6 20l2-4.5M18 20l-2-4.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>',
    "calendar": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="16" rx="2" stroke="currentColor" stroke-width="1.7"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "shield": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "bolt": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M13 3L5 13h6l-1 8 8-10h-6l1-8z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "pin": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 21s7-6.6 7-11.5a7 7 0 10-14 0C5 14.4 12 21 12 21z" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="9.5" r="2.4" stroke="currentColor" stroke-width="1.6"/></svg>',
    "mail": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2" stroke="currentColor" stroke-width="1.7"/><path d="M4 6.5l8 6 8-6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "phone": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M6 3h3l1.5 4-2 1.5a12 12 0 006 6l1.5-2 4 1.5v3a2 2 0 01-2.2 2A17 17 0 014 5.2 2 2 0 016 3z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "clock": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M12 7v5l3.5 2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
}


def form_hidden(subject, honey=True):
    """Hidden fields FormSubmit uses to route + format the email."""
    h = f"""      <input type="hidden" name="_subject" value="{subject}">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <!-- If your domain isn't live yet, change the line below to your github.io URL -->
      <input type="hidden" name="_next" value="{DOMAIN}/thanks.html">
"""
    if honey:
        h += '      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">\n'
    return h


def blog_card(href, img, cat, tag_label, title, excerpt):
    return f"""<article class="card">
        <a class="card-media" href="{href}"><img src="{img}" alt="{title}" loading="lazy"><span class="tag tag-{cat}">{tag_label}</span></a>
        <div class="card-body">
          <h3><a href="{href}">{title}</a></h3>
          <p>{excerpt}</p>
          <a class="more-link" href="{href}">Read more &rarr;</a>
        </div>
      </article>"""


# =========================================================
# HOME
# =========================================================
def page_home():
    html = head("Home", f"{CUP_NAME} is a {SEASON.lower()} soccer league for high school boys' and girls' teams — four divisions, weekly matches, and a championship weekend.")
    html += header("index.html")
    html += f"""
<section class="hero">
  <div class="hero-bg" style="background-image:url('images/hero.jpg')"></div>
  <div class="hero-overlay"></div>
  <div class="hero-inner">
    <p class="eyebrow light">{SEASON} &middot; Boys &amp; Girls High School Soccer</p>
    <h1>High school soccer<br><span class="accent">doesn't stop</span> in the fall.</h1>
    <p class="lede">{CUP_NAME} is a summer league built for high school teams &mdash; boys' and girls', varsity and JV. Weekly matches, certified officials, and a championship weekend worth training for.</p>
    <div class="hero-actions">
      <a href="register.html" class="btn btn-primary btn-lg">Register a Team</a>
      <a href="programs.html" class="btn btn-outline btn-lg">See Divisions</a>
    </div>
    <div class="stat-strip">
      <div class="stat-item"><strong>4</strong><span>Divisions</span></div>
      <div class="stat-item"><strong>9&ndash;12</strong><span>Grades eligible</span></div>
      <div class="stat-item"><strong>8</strong><span>Week season</span></div>
      <div class="stat-item"><strong>1</strong><span>Championship weekend</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">What is the {CUP_NAME}?</p>
        <h2>Summer soccer that actually counts.</h2>
        <p>Most high school players spend the summer scrimmaging in pickup games or waiting for preseason. {CUP_NAME} gives them somewhere real to play &mdash; a structured league with standings, officials, and a title on the line, running through the heart of the summer.</p>
        <p>Teams enter as school squads or as combined rosters of high school players. Boys' and girls' divisions run side by side, each split into varsity and JV so everyone competes at the right level.</p>
        <a href="about.html" class="btn btn-navy">More About the League</a>
      </div>
      <div class="split-media">
        <img src="images/about.jpg" alt="{CUP_NAME} high school summer soccer league" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">Divisions</p>
      <h2>Four divisions. One summer.</h2>
      <p class="lede mx-auto">Boys' and girls' brackets, each with varsity and JV play, for athletes in grades 9&ndash;12.</p>
    </div>
    <div class="grid grid-2">
      <article class="card card-feature">
        <a class="card-media" href="programs.html#boys"><img src="images/gallery/gallery-1.jpg" alt="Boys high school division" loading="lazy"><span class="tag tag-boys">Boys</span></a>
        <div class="card-body">
          <h3>Boys' High School Divisions</h3>
          <p>Varsity and JV brackets for boys in grades 9&ndash;12. Full 11v11 matches every week of the regular season.</p>
          <a class="more-link" href="programs.html#boys">Divisions &amp; format &rarr;</a>
        </div>
      </article>
      <article class="card card-feature">
        <a class="card-media" href="programs.html#girls"><img src="images/gallery/gallery-3.jpg" alt="Girls high school division" loading="lazy"><span class="tag tag-girls">Girls</span></a>
        <div class="card-body">
          <h3>Girls' High School Divisions</h3>
          <p>The same structure for girls' teams &mdash; varsity and JV brackets, weekly matches, and a shot at the Cup.</p>
          <a class="more-link" href="programs.html#girls">Divisions &amp; format &rarr;</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">How it works</p>
      <h2>Built like a real season</h2>
    </div>
    <div class="grid grid-3">
      <div class="feature">
        <div class="feature-icon">{ICON['calendar']}</div>
        <div><h3>Weekly Matches</h3><p>An eight-week regular season through June and July, scheduled by division.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['whistle']}</div>
        <div><h3>Certified Officials</h3><p>Every match is refereed and scored, with standings tracked all summer.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['trophy']}</div>
        <div><h3>{CUP_NAME} Weekend</h3><p>The season ends in a championship bracket &mdash; one title per division.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">From the League</p>
      <h2>News &amp; updates</h2>
    </div>
    <div class="grid grid-3">
      {blog_card("blog-registration-open.html", "images/blog/blog-1.jpg", "news", "News", f"Registration Is Open for {SEASON}", "Boys' and girls' divisions are open for high school teams. Here's what coaches need to know before entering a squad.")}
      {blog_card("blog-summer-prep.html", "images/blog/blog-2.jpg", "tips", "Players", "Using the Summer Before Fall Tryouts", "Five ways high school players can turn a summer season into a stronger fall with their school team.")}
      {blog_card("blog-coaches-guide.html", "images/blog/blog-3.jpg", "coaches", "Coaches", "A Coach's Guide to Entering a Team", "Roster rules, scheduling, and what your program is signing up for when you enter the Cup.")}
    </div>
    <div class="center" style="margin-top:36px;"><a href="blog.html" class="btn btn-navy">All Updates</a></div>
  </div>
</section>

<section>
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">Gallery</p>
      <h2>Around the league</h2>
    </div>
    <div class="grid grid-4 tight">
      {"".join(f'<a href="photos.html" class="thumb"><img src="images/gallery/gallery-{n}.jpg" alt="{CUP_NAME} gallery" loading="lazy"></a>' for n in [2, 5, 6, 8])}
    </div>
    <div class="center" style="margin-top:32px;"><a href="photos.html" class="btn btn-navy">Full Gallery</a></div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="cta-banner">
      <h2>Entering a team this summer?</h2>
      <p class="lede mx-auto">Registration is open for all four divisions. Tell us about your squad and we'll follow up with schedules, fees, and next steps.</p>
      <div class="cta-actions">
        <a href="register.html" class="btn btn-white btn-lg">Register a Team</a>
        <a href="tel:{PHONE_LINK}" class="btn btn-ghost btn-lg">{PHONE_DISPLAY}</a>
      </div>
    </div>
  </div>
</section>
"""
    html += footer()
    return html


write("index.html", page_home())


# =========================================================
# ABOUT
# =========================================================
def page_about():
    html = head("About", f"About {CUP_NAME} — a summer soccer league built for high school boys' and girls' teams.")
    html += header("about.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">About Us</p>
    <h1>Built for high school players.</h1>
    <p>{CUP_NAME} exists to fill the gap between school seasons with soccer worth showing up for.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div class="split-media">
        <img src="images/about.jpg" alt="{SITE_NAME} story" loading="lazy">
      </div>
      <div>
        <p class="eyebrow">Our Story</p>
        <h2>Why we started the {CUP_NAME}</h2>
        <p>High school soccer is short. A season ends in the fall, and then months go by before the next competitive match. Club soccer fills that gap for some players, but plenty of athletes &mdash; especially those who play for their school and not a club &mdash; end up with nowhere structured to play.</p>
        <p>{SITE_NAME} started with one goal: build a summer league that treats high school soccer seriously. Real schedules. Real officials. Standings that matter and a championship weekend that feels like one. Boys' and girls' divisions, varsity and JV, all running the same summer.</p>
        <p>It's soccer, it's high school, and that's the whole focus &mdash; no age groups to age out of, no watered-down format.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">What We're About</p>
      <h2>The standard we hold</h2>
    </div>
    <div class="grid grid-4">
      <div class="feature">
        <div class="feature-icon">{ICON['bolt']}</div>
        <div><h3>Real Competition</h3><p>A full season and a playoff bracket &mdash; not a weekend jamboree.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['users']}</div>
        <div><h3>School Squads Welcome</h3><p>Enter as a school team or as a combined roster of high school players.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['shield']}</div>
        <div><h3>Safe &amp; Officiated</h3><p>Certified referees on every match, with clear conduct standards for players and sidelines.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['ball']}</div>
        <div><h3>Ready for Fall</h3><p>Competitive minutes all summer so players arrive at preseason sharp.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="cta-banner">
      <h2>Want to get involved?</h2>
      <p class="lede mx-auto">Entering a team, coaching, officiating, or sponsoring &mdash; we'd like to hear from you.</p>
      <div class="cta-actions">
        <a href="register.html" class="btn btn-white btn-lg">Register a Team</a>
        <a href="contact.html" class="btn btn-ghost btn-lg">Contact Us</a>
      </div>
    </div>
  </div>
</section>
"""
    html += footer()
    return html


write("about.html", page_about())


# =========================================================
# DIVISIONS (programs.html)
# =========================================================
def division_table(rows):
    trs = "\n".join(
        f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows
    )
    return f"""<div class="table-wrap"><table class="age-table">
          <thead><tr><th>Division</th><th>Eligibility</th><th>Format</th></tr></thead>
          <tbody>{trs}</tbody>
        </table></div>"""


def page_programs():
    html = head("Divisions", f"{CUP_NAME} divisions: boys' and girls' varsity and JV high school soccer, season format, and championship weekend.")
    html += header("programs.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">Divisions</p>
    <h1>Boys' &amp; Girls' High School Soccer</h1>
    <p>Four divisions for athletes in grades 9&ndash;12, running one eight-week season with a championship weekend to close it out.</p>
  </div>
</section>

<section>
  <div class="container">
    <div id="boys" class="league-block boys">
      <div class="league-head">
        <div>
          <span class="tag tag-boys">Boys</span>
          <h2>Boys' High School Divisions</h2>
        </div>
        <a href="register.html" class="btn btn-primary btn-sm">Register a Boys' Team</a>
      </div>
      <p>Varsity and JV brackets for boys in grades 9&ndash;12. Teams may enter as a school squad or as a combined roster of high school players from the same area.</p>
      {division_table([
          ("Boys Varsity", "Grades 9&ndash;12", "11v11, full pitch, two 40-minute halves"),
          ("Boys JV", "Grades 9&ndash;11", "11v11, full pitch, two 35-minute halves"),
      ])}
    </div>

    <div id="girls" class="league-block girls">
      <div class="league-head">
        <div>
          <span class="tag tag-girls">Girls</span>
          <h2>Girls' High School Divisions</h2>
        </div>
        <a href="register.html" class="btn btn-primary btn-sm">Register a Girls' Team</a>
      </div>
      <p>The same structure for girls' teams &mdash; varsity and JV brackets, weekly matches, and a place in the championship bracket at the end of the summer.</p>
      {division_table([
          ("Girls Varsity", "Grades 9&ndash;12", "11v11, full pitch, two 40-minute halves"),
          ("Girls JV", "Grades 9&ndash;11", "11v11, full pitch, two 35-minute halves"),
      ])}
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">Season Format</p>
      <h2>How the summer runs</h2>
    </div>
    <div class="grid grid-4">
      <div class="feature">
        <div class="feature-icon">{ICON['calendar']}</div>
        <div><h3>Eight Weeks</h3><p>A regular season across June and July, one match per week per team.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['whistle']}</div>
        <div><h3>Officiated Play</h3><p>Certified referees on every match, with results and standings published weekly.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['users']}</div>
        <div><h3>Roster Flexibility</h3><p>Squads of up to 22 players, all currently enrolled in grades 9&ndash;12.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['trophy']}</div>
        <div><h3>Championship Weekend</h3><p>Every division plays a bracket in August &mdash; four champions, one Cup weekend.</p></div>
      </div>
    </div>
    <p class="center fine-print">Exact dates, fields and fees are confirmed with each team at registration.</p>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="cta-banner">
      <h2>Registration is open for {SEASON}</h2>
      <p class="lede mx-auto">Enter your team, ask about a division, or find out how to get a new squad started.</p>
      <div class="cta-actions">
        <a href="register.html" class="btn btn-white btn-lg">Register a Team</a>
        <a href="mailto:{EMAIL}" class="btn btn-ghost btn-lg">{EMAIL}</a>
      </div>
    </div>
  </div>
</section>
"""
    html += footer()
    return html


write("programs.html", page_programs())


# =========================================================
# REGISTER
# =========================================================
FAQ = [
    ("Who is eligible to play?",
     "Any athlete currently enrolled in grades 9&ndash;12 for the upcoming school year. Teams can be school squads or combined rosters of high school players."),
    ("Do we need to enter a full team?",
     "Yes &mdash; the Cup is a team competition. If you have a partial roster, get in touch and we'll try to connect you with other players in your area."),
    ("When does the season run?",
     "The regular season runs eight weeks through June and July, with championship weekend in August. Exact dates are confirmed with teams at registration."),
    ("What does it cost?",
     "Fees depend on division and field costs for the season. We'll send the current fee schedule when we follow up on your registration."),
    ("Who coaches the teams?",
     "Teams bring their own coach or team manager. If you're a coach looking for a squad, mention it in the form and we'll keep you in mind."),
    ("Is registration final when I submit this form?",
     "No. This form starts the process &mdash; we'll reply by email to confirm your division, dates, and fees before anything is locked in."),
]


def faq_block(items):
    out = []
    for q, a in items:
        out.append(f"""<details class="faq-item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>""")
    return "\n      ".join(out)


def page_register():
    html = head("Register a Team", f"Register a high school boys' or girls' team for the {SEASON} {CUP_NAME} soccer league.")
    html += header("register.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">Registration</p>
    <h1>Register Your Team</h1>
    <p>Tell us about your squad and we'll follow up by email with divisions, dates, and fees. Nothing is locked in until we confirm with you.</p>
  </div>
</section>

<section>
  <div class="container narrow">
    <form class="contact-form card-form" action="{FORM_ENDPOINT}" method="POST">
{form_hidden(f"New {CUP_NAME} team registration")}      <div class="form-grid">
        <div class="full">
          <label for="team">Team or school name <span class="req">*</span></label>
          <input id="team" name="Team or school" type="text" required autocomplete="organization">
        </div>
        <div>
          <label for="division">Division <span class="req">*</span></label>
          <select id="division" name="Division" required>
            <option value="">Choose a division…</option>
            <option>Boys Varsity</option>
            <option>Boys JV</option>
            <option>Girls Varsity</option>
            <option>Girls JV</option>
            <option>Not sure yet</option>
          </select>
        </div>
        <div>
          <label for="roster">Approximate roster size</label>
          <input id="roster" name="Roster size" type="number" min="1" max="30" placeholder="e.g. 18">
        </div>
        <div>
          <label for="name">Coach / contact name <span class="req">*</span></label>
          <input id="name" name="Contact name" type="text" required autocomplete="name">
        </div>
        <div>
          <label for="role">Your role</label>
          <select id="role" name="Role">
            <option>Head coach</option>
            <option>Assistant coach</option>
            <option>Team manager</option>
            <option>Parent / guardian</option>
            <option>Player</option>
            <option>Other</option>
          </select>
        </div>
        <div>
          <label for="email">Email <span class="req">*</span></label>
          <input id="email" name="Email" type="email" required autocomplete="email">
        </div>
        <div>
          <label for="phone">Phone</label>
          <input id="phone" name="Phone" type="tel" autocomplete="tel">
        </div>
        <div class="full">
          <label for="town">Town / area</label>
          <input id="town" name="Town" type="text" placeholder="Where your team is based">
        </div>
        <div class="full">
          <label for="message">Anything else we should know?</label>
          <textarea id="message" name="Notes" placeholder="Scheduling constraints, questions about a division, whether you need help filling a roster…"></textarea>
        </div>
        <div class="full">
          <button type="submit" class="btn btn-primary btn-lg">Submit Registration</button>
          <p class="form-note">We'll reply to the email address above. Questions first? Call <a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
          <div class="form-success"></div>
        </div>
      </div>
    </form>
  </div>
</section>

<section class="band">
  <div class="container narrow">
    <div class="center stack">
      <p class="eyebrow">Questions</p>
      <h2>Before you register</h2>
    </div>
    <div class="faq">
      {faq_block(FAQ)}
    </div>
  </div>
</section>
"""
    html += footer()
    return html


write("register.html", page_register())


# =========================================================
# THANK YOU
# =========================================================
def page_thanks():
    html = head("Thanks", "Your message has been received by Arrow Athletics.")
    html += header("")
    html += f"""
<section class="page-hero tall">
  <div class="container">
    <div class="check-mark">{ICON['trophy']}</div>
    <h1>Got it &mdash; thank you.</h1>
    <p>Your message is on its way to our inbox. We reply to most registrations and enquiries within a couple of days.</p>
    <div class="cta-actions center-actions">
      <a href="index.html" class="btn btn-white btn-lg">Back to Home</a>
      <a href="programs.html" class="btn btn-ghost btn-lg">See Divisions</a>
    </div>
    <p class="fine-print light-print">Need something sooner? Call {PHONE_DISPLAY} or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</section>
"""
    html += footer()
    return html


write("thanks.html", page_thanks())


# =========================================================
# PHOTOS
# =========================================================
GALLERY_ITEMS = [
    (1, "boys", "boys", "Boys", "Boys Varsity &mdash; opening week"),
    (2, "matchday", "cup", "Matchday", "Warmups before kickoff"),
    (3, "girls", "girls", "Girls", "Girls Varsity &mdash; league play"),
    (4, "matchday", "cup", "Matchday", "Sideline view, midweek fixture"),
    (5, "girls", "girls", "Girls", "Girls JV &mdash; Saturday fixtures"),
    (6, "boys", "boys", "Boys", "Boys JV &mdash; second half"),
    (7, "championship", "cup", "Championship", "Championship weekend"),
    (8, "championship", "cup", "Championship", "Trophy presentation"),
]


def gallery_item(n, category, tagcls, label, caption):
    return f"""<figure class="gallery-item" data-category="{category}">
      <img src="images/gallery/gallery-{n}.jpg" alt="{caption}" loading="lazy">
      <span class="tag tag-{tagcls}">{label}</span>
      <figcaption class="gallery-cap">{caption}</figcaption>
    </figure>"""


def page_photos():
    html = head("Photos", f"Photos from the {CUP_NAME} — boys' and girls' high school matches, matchdays, and championship weekend.")
    html += header("photos.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">Gallery</p>
    <h1>Around the League</h1>
    <p>Matchdays, league fixtures, and championship weekend across the boys' and girls' divisions.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="filter-bar">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="boys">Boys</button>
      <button class="filter-btn" data-filter="girls">Girls</button>
      <button class="filter-btn" data-filter="matchday">Matchday</button>
      <button class="filter-btn" data-filter="championship">Championship</button>
    </div>
    <div class="gallery-grid">
      {"".join(gallery_item(*item) for item in GALLERY_ITEMS)}
    </div>
    <p class="center fine-print">Season photography coming as the summer gets underway &mdash; the graphics above are placeholders.</p>
  </div>
</section>
{lightbox()}
"""
    html += footer()
    return html


write("photos.html", page_photos())


# =========================================================
# BLOG
# =========================================================
BLOG_POSTS = [
    {
        "slug": "blog-registration-open.html",
        "img": "images/blog/blog-1.jpg",
        "cat": "news", "tag": "News",
        "title": f"Registration Is Open for {SEASON}",
        "date": f"June 1, {YEAR}",
        "excerpt": "Boys' and girls' divisions are open for high school teams. Here's what coaches need to know before entering a squad.",
    },
    {
        "slug": "blog-summer-prep.html",
        "img": "images/blog/blog-2.jpg",
        "cat": "tips", "tag": "Players",
        "title": "Using the Summer Before Fall Tryouts",
        "date": f"June 8, {YEAR}",
        "excerpt": "Five ways high school players can turn a summer season into a stronger fall with their school team.",
    },
    {
        "slug": "blog-coaches-guide.html",
        "img": "images/blog/blog-3.jpg",
        "cat": "coaches", "tag": "Coaches",
        "title": "A Coach's Guide to Entering a Team",
        "date": f"June 15, {YEAR}",
        "excerpt": "Roster rules, scheduling, and what your program is signing up for when you enter the Cup.",
    },
]


def page_blog():
    html = head("News", f"News and updates from the {CUP_NAME} high school summer soccer league.")
    html += header("blog.html")
    cards = "".join(
        blog_card(p["slug"], p["img"], p["cat"], p["tag"], p["title"], p["excerpt"]) for p in BLOG_POSTS
    )
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">News</p>
    <h1>League News &amp; Updates</h1>
    <p>Registration news, player guidance, and updates from around the {CUP_NAME}.</p>
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


def article(slug, img, cat, tag, title, date, body):
    html = head(title, f"{title} — {CUP_NAME} news.")
    html += header("blog.html")
    body_html = "\n".join(
        f"<h2>{p[1]}</h2>" if p[0] == "h2"
        else f"<p>{p[1]}</p>" if p[0] == "p"
        else ("<ul>" + "".join(f"<li>{li}</li>" for li in p[1]) + "</ul>")
        for p in body
    )
    html += f"""
<section class="article-hero">
  <div class="container">
    <a href="blog.html" class="back-link">&larr; All updates</a>
    <span class="tag tag-{cat}">{tag}</span>
    <h1>{title}</h1>
    <p class="article-meta">{date}</p>
  </div>
  <div class="article-cover"><img src="{img}" alt="{title}"></div>
</section>
<section>
  <div class="container">
    <article class="article-body">
      {body_html}
      <div class="article-cta">
        <h3>Ready to enter a team?</h3>
        <p>Registration for {SEASON} is open for all four divisions.</p>
        <a href="register.html" class="btn btn-primary">Register a Team</a>
      </div>
    </article>
  </div>
</section>
"""
    html += footer()
    write(slug, html)


article(
    "blog-registration-open.html", "images/blog/blog-1.jpg", "news", "News",
    f"Registration Is Open for {SEASON}", f"June 1, {YEAR}",
    [
        ("p", f"Registration for the {SEASON} {CUP_NAME} is open. Four divisions are running this summer &mdash; boys' varsity, boys' JV, girls' varsity and girls' JV &mdash; all for athletes in grades 9&ndash;12."),
        ("h2", "What a team gets"),
        ("p", "Every registered team plays a full eight-week regular season with officiated matches, published standings, and a place in the championship bracket in August."),
        ("ul", [
            "Weekly 11v11 fixtures through June and July",
            "Certified referees on every match",
            "Standings tracked and published through the season",
            "A guaranteed spot in championship weekend",
        ]),
        ("h2", "Who can enter"),
        ("p", "Teams can enter as a school squad or as a combined roster of high school players from the same area. Every player must be enrolled in grades 9&ndash;12 for the upcoming school year. Rosters can carry up to 22 players."),
        ("h2", "How to register"),
        ("p", "Fill out the registration form with your team name, division, and a contact for the coach or manager. We'll reply by email with the season schedule, field locations, and the current fee schedule before anything is confirmed."),
        ("p", "Divisions are capped, so teams that register early get first choice of match slots."),
    ],
)

article(
    "blog-summer-prep.html", "images/blog/blog-2.jpg", "tips", "Players",
    "Using the Summer Before Fall Tryouts", f"June 8, {YEAR}",
    [
        ("p", "A summer league is only as valuable as what you do with it. Here are five ways high school players get the most out of a season in the Cup before returning to their school team in the fall."),
        ("h2", "1. Play a position you want to own"),
        ("p", "Summer is the low-risk window to get real minutes somewhere new. If you want to move into midfield in the fall, this is the season to prove you can do it."),
        ("h2", "2. Build the fitness base now"),
        ("p", "Preseason is a brutal place to start getting fit. Players who arrive in August already carrying eight weeks of match fitness spend preseason competing instead of surviving."),
        ("h2", "3. Treat every match like it's scouted"),
        ("p", "Your school coach hears about summer form &mdash; from you, from teammates, from other coaches in the area. Consistency across a season says more than one good game."),
        ("h2", "4. Learn to lead"),
        ("p", "Summer rosters mix players from different programs, which makes communication harder and more valuable. Players who organize a back line in July tend to wear the armband in October."),
        ("h2", "5. Actually recover"),
        ("p", "Eight weeks of matches in summer heat is a real load. Hydration, sleep, and at least one genuine rest day a week are what keep a strong summer from turning into an injured fall."),
    ],
)

article(
    "blog-coaches-guide.html", "images/blog/blog-3.jpg", "coaches", "Coaches",
    "A Coach's Guide to Entering a Team", f"June 15, {YEAR}",
    [
        ("p", "If you're considering entering a squad in the Cup this summer, here's what the commitment actually looks like."),
        ("h2", "Rosters"),
        ("p", "Squads carry up to 22 players, all enrolled in grades 9&ndash;12 for the coming school year. You can enter a full school team or build a combined roster from players across a town or region."),
        ("h2", "The schedule"),
        ("p", "One match per week per team across an eight-week regular season, then championship weekend in August. We work around the obvious summer conflicts &mdash; camps, vacations, and team commitments &mdash; where we can, so tell us about them at registration."),
        ("h2", "What you're responsible for"),
        ("ul", [
            "Naming a coach or team manager as the league contact",
            "Submitting a roster before the first fixture",
            "Getting your squad to matches on time and ready to play",
            "Sideline conduct &mdash; yours, your players', and your spectators'",
        ]),
        ("h2", "What we handle"),
        ("p", "Scheduling, fields, certified officials, standings, and the championship bracket. You coach; we run the league."),
        ("h2", "Coaches without a team"),
        ("p", "If you want to coach but don't have a squad, get in touch anyway. We hear from players looking for teams every summer and we're happy to make the connection."),
    ],
)


# =========================================================
# CONTACT
# =========================================================
def page_contact():
    html = head("Contact", f"Contact {CUP_NAME} — email {EMAIL} or call {PHONE_DISPLAY}.")
    html += header("contact.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">Contact</p>
    <h1>Get In Touch</h1>
    <p>Questions about divisions, coaching, officiating or sponsorship &mdash; we're happy to talk.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="contact-layout">
      <aside class="contact-info-card">
        <h3>Contact Info</h3>
        <div class="contact-row">
          <span class="ic">{ICON['mail']}</span>
          <div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div>
        </div>
        <div class="contact-row">
          <span class="ic">{ICON['phone']}</span>
          <div><strong>Phone</strong><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a></div>
        </div>
        <div class="contact-row">
          <span class="ic">{ICON['clock']}</span>
          <div><strong>Season</strong><span>{SEASON} &middot; registration open</span></div>
        </div>
        <div class="contact-row">
          <span class="ic">{ICON['trophy']}</span>
          <div><strong>Entering a team?</strong><a href="register.html">Use the registration form &rarr;</a></div>
        </div>
        <div class="social-row">
          <a href="#" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.8"/></svg></a>
          <a href="#" aria-label="Facebook"><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M15 8.5h2V5h-2c-2.2 0-4 1.8-4 4v2H9v3.5h2V21h3.5v-6.5H17l.5-3.5h-3V9c0-.6.4-1 1-1z" fill="currentColor"/></svg></a>
        </div>
      </aside>

      <div>
        <h2>Send a Message</h2>
        <form class="contact-form" action="{FORM_ENDPOINT}" method="POST">
{form_hidden(f"New {SITE_NAME} website enquiry")}          <div class="form-grid">
            <div>
              <label for="cname">Name <span class="req">*</span></label>
              <input id="cname" name="Name" type="text" required autocomplete="name">
            </div>
            <div>
              <label for="cemail">Email <span class="req">*</span></label>
              <input id="cemail" name="Email" type="email" required autocomplete="email">
            </div>
            <div>
              <label for="cphone">Phone</label>
              <input id="cphone" name="Phone" type="tel" autocomplete="tel">
            </div>
            <div>
              <label for="ctopic">I'm asking about</label>
              <select id="ctopic" name="Topic">
                <option>Entering a team</option>
                <option>Coaching</option>
                <option>Refereeing / officials</option>
                <option>Sponsorship</option>
                <option>Something else</option>
              </select>
            </div>
            <div class="full">
              <label for="cmessage">Message <span class="req">*</span></label>
              <textarea id="cmessage" name="Message" required placeholder="How can we help?"></textarea>
            </div>
            <div class="full">
              <button type="submit" class="btn btn-primary btn-lg">Send Message</button>
              <div class="form-success"></div>
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
    html = head("Page Not Found", "That page doesn't exist — head back to Arrow Athletics.")
    html += header("")
    html += f"""
<section class="page-hero tall">
  <div class="container">
    <p class="eyebrow light">404</p>
    <h1>Offside &mdash; that page doesn't exist.</h1>
    <p>The page you're after was moved, renamed, or never existed.</p>
    <div class="cta-actions center-actions">
      <a href="index.html" class="btn btn-white btn-lg">Back to Home</a>
      <a href="register.html" class="btn btn-ghost btn-lg">Register a Team</a>
    </div>
  </div>
</section>
"""
    html += footer()
    return html


write("404.html", page_404())

print("\nAll pages built.")
