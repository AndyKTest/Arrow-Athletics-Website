#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds every static HTML page for the Arrow Athletics / Arrow Cup site from
shared partials, so the nav, branding and footer stay identical across pages.

Run from the repo root:   python3 dev-tools/build.py
"""
import os

SITE_NAME = "Arrow Athletics"          # the organization
LEAGUE_NAME = "Arrow League"           # the summer league itself
CUP_NAME = "Arrow Cup"                 # the end-of-season knockout tournament
SEASON = "Summer 2027"                 # first season
STATE = "Massachusetts"
PRICE = "<span class=\"nowrap\">$1,700&ndash;$1,850</span>"          # team price range (from the coaches deck)
TAGLINE = "Hit Your Target"
CTA_LABEL = "Interested in Participating?"   # main call to action -> register.html (interest form)
YEAR = "2026"                          # copyright year fallback (main.js updates it)
EMAIL = "info@arrow-athletics.com"
PHONE_DISPLAY = "+1 (774) 270-9555"
PHONE_LINK = "+17742709555"
DOMAIN = "https://arrow-athletics.com"
INSTAGRAM_HANDLE = "arrowathleticss"
INSTAGRAM_URL = f"https://instagram.com/{INSTAGRAM_HANDLE}"

# Where registration + contact submissions are emailed.
# FormSubmit relays the submission straight to the address below — no account needed.
FORM_ENDPOINT = f"https://formsubmit.co/{EMAIL}"

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("programs.html", "Divisions"),
    ("photos.html", "Photos"),
    ("merch.html", "Merch"),
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
        <li class="nav-cta"><a href="register.html" class="btn btn-primary btn-sm">{CTA_LABEL}</a></li>
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
        <p>The {LEAGUE_NAME} is a summer soccer league for high school boys' and girls' teams across {STATE} &mdash; six divisions, real referees, and the {CUP_NAME} to finish the summer.</p>
        <div class="social-row">
          <a href="{INSTAGRAM_URL}" aria-label="Instagram" title="@{INSTAGRAM_HANDLE} on Instagram" target="_blank" rel="noopener">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.8"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>
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
          <li><a href="register.html">{CTA_LABEL}</a></li>
          <li><a href="contact.html">Coach &amp; Referee Inquiries</a></li>
          <li><a href="contact.html">Sponsor the League</a></li>
          <li><a href="contact.html">General Questions</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a></li>
          <li><a href="{INSTAGRAM_URL}" target="_blank" rel="noopener">@{INSTAGRAM_HANDLE}</a></li>
          <li><span>{SEASON} &middot; Registration opens soon</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>{YEAR}</span> {SITE_NAME}. All rights reserved.</span>
      <span>{TAGLINE}.</span>
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
    "home": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M4 11l8-6.5 8 6.5V20a1 1 0 01-1 1h-4.5v-5.5h-5V21H5a1 1 0 01-1-1v-9z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "levels": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M5 20v-5M12 20V10M19 20V4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>',
    "cap": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M2.5 9.5L12 5l9.5 4.5L12 14 2.5 9.5z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M6.5 11.5V16c0 1.4 2.5 3 5.5 3s5.5-1.6 5.5-3v-4.5M21.5 9.5V15" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "map": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M9 4L3.5 6v14L9 18l6 2 5.5-2V4L15 6 9 4z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 4v14M15 6v14" stroke="currentColor" stroke-width="1.7"/></svg>',
    "check": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M5 12.5l4.5 4.5L19 7.5" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "instagram": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><circle cx="17.5" cy="6.5" r="1.1" fill="currentColor"/></svg>',
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




# =========================================================
# SHARED LEAGUE CONTENT (kept in step with the coaches deck)
# =========================================================
LEAGUE_ABOUT = (f"The {LEAGUE_NAME} brings together high school boys and girls across {STATE}, giving them a chance "
                "to keep playing through the summer offseason. With a structured format, clear guidelines, a divisional "
                "setup and referees, the league turns casual summer pickup into a consistent opportunity to sharpen your "
                "skills, build team chemistry, and get reps with others who love the game.")

DIVISIONS = [
    ("Division 1", "Top-level competition"),
    ("Division 2", "Competitive play for rising teams"),
    ("Division 3", "Development and building experience"),
]
MATCH_FORMAT = "11v11 &middot; two 40-minute halves"

WHY = [
    ("home", "Your school, your summer", "Keep your team together and keep representing your school, with your own players and your own coaches."),
    ("levels", "Play at your level", "We work with each team to find the right division, so every team finds games that fit."),
    ("bolt", "Stay sharp for fall", "Ten games over five weeks keep your players in rhythm heading into the fall season."),
    ("cap", "College coach exposure", "Put your players in front of college coaches and into the recruiting conversation."),
    ("map", "Best team in the state", f"Compete against teams from across {STATE} to find out who the best team in the state really is."),
    ("whistle", "We run the league", "Scheduling, referees and standings are handled by us, so you can focus on coaching, playing and developing."),
]

SEASON_STEPS = [
    ("Get placed in a division", ["Work with our coordinators to find the right fit",
                                  "Boys and girls each have Divisions 1, 2 and 3",
                                  "Each division is split into pools"]),
    ("Pool play", ["Five weeks, July into August",
                   "Two weekday games a week, 4 to 9 p.m.",
                   f"Pool results decide who advances to the {CUP_NAME}"]),
    (f"The {CUP_NAME}", ["A knockout bracket on the final weekend of the season",
                         "Top teams from each pool face off over three days",
                         "Every game is win or go home"]),
    ("Six champions", ["One title for each division",
                       "Boys and girls Divisions 1, 2 and 3",
                       f"Medals, a trophy, and the honor of winning the {CUP_NAME}"]),
]

INCLUDED_STATS = [("40", "Minute halves"), ("1", "Referee per game"), ("30", "Players max per roster"), ("2+", "Captains per team")]

FOUNDERS = [
    ("images/team/andrew.jpg", "Andrew Kovacs", [
        "10 years of club soccer at Boston Bolts",
        "Four-year varsity player and team captain at St. John&rsquo;s High School, Shrewsbury",
        "Four years at Worcester Polytechnic Institute, serving as team captain",
        "Graduated in May 2025",
    ]),
    ("images/team/greg.jpg", "Gregory Kovacs", [
        "10 years of club soccer at Boston Bolts",
        "Four-year varsity player and team captain at St. John&rsquo;s High School, Shrewsbury",
        "Currently playing club soccer at Fairfield University",
        "Graduating in May 2027",
    ]),
]


def ul(items, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def cta_banner(title, text, secondary_href=None, secondary_label=None):
    second = ""
    if secondary_href:
        second = f'\n        <a href="{secondary_href}" class="btn btn-ghost btn-lg">{secondary_label}</a>'
    return f"""
<section class="section-tight">
  <div class="container">
    <div class="cta-banner">
      <h2>{title}</h2>
      <p class="lede mx-auto">{text}</p>
      <div class="cta-actions">
        <a href="register.html" class="btn btn-white btn-lg">{CTA_LABEL}</a>{second}
      </div>
    </div>
  </div>
</section>
"""


# =========================================================
# HOME
# =========================================================
def page_home():
    html = head("Home", f"The {LEAGUE_NAME} is a summer soccer league for high school boys' and girls' teams across {STATE}: six divisions, ten games in five weeks, and the {CUP_NAME}.")
    html += header("index.html")
    html += f"""
<section class="hero">
  <div class="hero-bg" style="background-image:url('images/hero.jpg')"></div>
  <div class="hero-overlay"></div>
  <div class="hero-inner">
    <p class="eyebrow light">Est. {SEASON} &middot; {STATE} &middot; Boys &amp; Girls</p>
    <h1>High school soccer<br><span class="accent">doesn't stop</span> in the fall.</h1>
    <p class="lede">The {LEAGUE_NAME} is a summer league for high school boys' and girls' teams across {STATE}. Ten games in five weeks, a referee on every game, and the {CUP_NAME} to play for.</p>
    <div class="hero-actions">
      <a href="register.html" class="btn btn-primary btn-lg">{CTA_LABEL}</a>
      <a href="programs.html" class="btn btn-outline btn-lg">See Divisions</a>
    </div>
    <div class="stat-strip">
      <div class="stat-item"><strong>6</strong><span>Divisions</span></div>
      <div class="stat-item"><strong>5</strong><span>Week season</span></div>
      <div class="stat-item"><strong>10</strong><span>Games per team</span></div>
      <div class="stat-item"><strong>6</strong><span>Champions crowned</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <p class="eyebrow">What is the {LEAGUE_NAME}?</p>
        <h2>Summer soccer that actually counts.</h2>
        <p>{LEAGUE_ABOUT}</p>
        <p>Boys' and girls' teams each play in Division 1, 2 or 3, and our league coordinators work with every team to find the right fit.</p>
        <a href="about.html" class="btn btn-navy">Meet the Founders</a>
      </div>
      <div class="split-media">
        <img src="images/about.jpg" alt="High school team huddle before a game" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">Divisions</p>
      <h2>Six divisions. One summer.</h2>
      <p class="lede mx-auto">Divisions 1, 2 and 3 for both boys' and girls' high school teams.</p>
    </div>
    <div class="grid grid-2">
      <article class="card card-feature">
        <a class="card-media" href="programs.html#boys"><img src="images/gallery/gallery-16.jpg" alt="Boys high school soccer action" loading="lazy"><span class="tag tag-boys">Boys</span></a>
        <div class="card-body">
          <h3>Boys' Divisions</h3>
          <p>Divisions 1, 2 and 3 for boys' high school teams. Full 11v11 games with 40-minute halves, two weeknights a week.</p>
          <a class="more-link" href="programs.html#boys">Divisions &amp; format &rarr;</a>
        </div>
      </article>
      <article class="card card-feature">
        <a class="card-media" href="programs.html#girls"><img src="images/gallery/gallery-3.jpg" alt="Girls high school soccer action" loading="lazy"><span class="tag tag-girls">Girls</span></a>
        <div class="card-body">
          <h3>Girls' Divisions</h3>
          <p>The same structure for girls' teams: Divisions 1, 2 and 3, two games a week, and a shot at the {CUP_NAME}.</p>
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
        <div><h3>Two Games a Week</h3><p>Five weeks of pool play from July into August, on weeknights between 4 and 9 p.m.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['whistle']}</div>
        <div><h3>A Referee Every Game</h3><p>We handle scheduling, referees and standings, so teams can focus on playing.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['trophy']}</div>
        <div><h3>The {CUP_NAME}</h3><p>Top teams from each pool meet in a knockout bracket on the final weekend. Six divisions, six champions.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">Gallery</p>
      <h2>On the field</h2>
    </div>
    <div class="grid grid-4 tight">
      {"".join(f'<a href="photos.html" class="thumb"><img src="images/gallery/gallery-{n}.jpg" alt="High school soccer photo" loading="lazy"></a>' for n in [18, 5, 15, 17])}
    </div>
    <div class="center" style="margin-top:32px;"><a href="photos.html" class="btn btn-navy">Full Gallery</a></div>
  </div>
</section>
"""
    html += cta_banner(CTA_LABEL,
                       f"Registration for {SEASON} opens soon. Tell us about your team and we'll take a look and follow up with divisions, dates and next steps.",
                       f"tel:{PHONE_LINK}", PHONE_DISPLAY)
    html += footer()
    return html


write("index.html", page_home())


# =========================================================
# ABOUT
# =========================================================
def founder_card(img, name, bullets):
    return f"""<article class="founder-card">
        <img src="{img}" alt="{name} headshot" loading="lazy">
        <div>
          <div class="founder-head"><h3>{name}</h3><span class="role-pill">Co-Founder</span></div>
          {ul(bullets, "founder-list")}
        </div>
      </article>"""


def page_about():
    html = head("About", f"Who we are: {SITE_NAME} was founded by brothers Andrew and Greg Kovacs to give high school players in {STATE} a real summer league.")
    html += header("about.html")
    why_html = "\n      ".join(
        f'<div class="feature"><div class="feature-icon">{ICON[ic]}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
        for ic, t, d in WHY)
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">About Us</p>
    <h1>Who we are</h1>
    <p>{SITE_NAME} is a newly formed organization built to give high school boys and girls a unique opportunity to compete over the summer.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div class="split-media">
        <img class="tall-photo" src="images/gallery/gallery-13.jpg" alt="Two St. John's players with family on the field on a fall day" loading="lazy">
      </div>
      <div>
        <p class="eyebrow">Our Story</p>
        <h2>Why we started the {LEAGUE_NAME}</h2>
        <p>My brother Greg and I started {SITE_NAME} because, like a lot of the players who'll fill these divisions, we loved playing for our high school team &mdash; and we missed it the second the fall season ended. We both went on to play in college, and we watched plenty of teammates go the club route too. That's real competition, and we don't take anything away from it. But none of it replaces playing for your school, with your own classmates on the sideline cheering you on.</p>
        <p>So we built the league we wished had existed: a summer season where high school players keep playing as a team, with real divisions, real referees, and standings that actually matter &mdash; not a pickup run to kill time before preseason.</p>
        <p>Our first season, {SEASON}, brings together high school teams from across {STATE}. Teams play the season in pools, then meet on the final weekend for the {CUP_NAME}, where the top teams from each pool play for the title. Over time we want to grow it across New England, bringing together high school teams that have never had a reason, or a chance, to play each other.</p>
        <p class="signoff">&mdash; Andrew Kovacs, Co-Founder</p>
      </div>
    </div>
  </div>
</section>

<section class="mission-band">
  <div class="container narrow center">
    <p class="eyebrow light">Our Mission</p>
    <p class="mission-text">A high-quality summer league that builds stronger players, better teams, and a greater sense of connection to all competition.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">The Founders</p>
      <h2>Meet Andrew and Greg</h2>
      <p class="lede mx-auto">Two brothers who have always had a passion for the beautiful game. After playing at the collegiate level, they're using {SITE_NAME} to pay it forward to the next generation of competitors.</p>
    </div>
    <div class="founders">
      <div class="founders-photo">
        <img src="images/gallery/gallery-14.jpg" alt="Andrew smiling with a leadership award plaque between two teammates, one holding a State Champions jacket" loading="lazy">
      </div>
      <div class="founders-cards">
      {"".join(founder_card(*f) for f in FOUNDERS)}
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">Why the {LEAGUE_NAME}</p>
      <h2>Why choose the {LEAGUE_NAME}</h2>
    </div>
    <div class="grid grid-3">
      {why_html}
    </div>
    <p class="center why-close">And the {CUP_NAME} to play for, with a champion crowned in every division.</p>
  </div>
</section>
"""
    html += cta_banner("Want a walkthrough?",
                       "We're happy to set up a call or in-person meeting to answer any questions about the league.",
                       "contact.html", "Contact Us")
    html += footer()
    return html


write("about.html", page_about())


# =========================================================
# DIVISIONS (programs.html)
# =========================================================
def division_table(prefix):
    trs = "\n".join(
        f"<tr><td><strong>{prefix} {d}</strong></td><td>{lvl}</td><td>{MATCH_FORMAT}</td></tr>" for d, lvl in DIVISIONS
    )
    return f"""<div class="table-wrap"><table class="age-table">
          <thead><tr><th>Division</th><th>Level</th><th>Format</th></tr></thead>
          <tbody>{trs}</tbody>
        </table></div>"""


def page_programs():
    html = head("Divisions", f"{LEAGUE_NAME} divisions: Divisions 1, 2 and 3 for high school boys' and girls' teams in {STATE}, season format, and what's included.")
    html += header("programs.html")
    steps = "\n      ".join(
        f'<div class="step-card"><span class="step-num">{i}</span><h3>{t}</h3>{ul(items)}</div>'
        for i, (t, items) in enumerate(SEASON_STEPS, 1))
    stats = "".join(f'<div class="stat-tile"><strong>{n}</strong><span>{l}</span></div>' for n, l in INCLUDED_STATS)
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">Divisions</p>
    <h1>Boys' &amp; Girls' Divisions</h1>
    <p>Six divisions across {STATE}: Divisions 1, 2 and 3 for boys and for girls. Five weeks of pool play, then the {CUP_NAME}.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="center stack intro-block">
      <p class="eyebrow">What is the {LEAGUE_NAME}?</p>
      <p class="lede mx-auto">{LEAGUE_ABOUT}</p>
    </div>

    <div id="boys" class="league-block boys">
      <div class="league-head">
        <div>
          <span class="tag tag-boys">Boys</span>
          <h2>Boys' Divisions</h2>
        </div>
        <a href="register.html" class="btn btn-primary btn-sm">{CTA_LABEL}</a>
      </div>
      <p>Divisions 1, 2 and 3 for boys' high school teams. Each division is split into pools for the regular season.</p>
      <div class="league-photo"><img src="images/gallery/gallery-4.jpg" alt="Boys high school soccer action" loading="lazy"></div>
      {division_table("Boys")}
    </div>

    <div id="girls" class="league-block girls">
      <div class="league-head">
        <div>
          <span class="tag tag-girls">Girls</span>
          <h2>Girls' Divisions</h2>
        </div>
        <a href="register.html" class="btn btn-primary btn-sm">{CTA_LABEL}</a>
      </div>
      <p>The same structure for girls' teams: Divisions 1, 2 and 3, each split into pools, with a place in the {CUP_NAME} bracket on the final weekend.</p>
      <div class="league-photo"><img src="images/gallery/gallery-5.jpg" alt="Girls high school soccer action" loading="lazy"></div>
      {division_table("Girls")}
    </div>
    <p class="center fine-print">Not sure where your team fits? Our league coordinators work with every team to find the right division.</p>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">Season Format</p>
      <h2>How the summer runs</h2>
    </div>
    <div class="steps grid-4">
      {steps}
    </div>
    <p class="center why-close">Six divisions. Six champions.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">What's Included</p>
      <h2>What every team gets</h2>
    </div>
    <div class="stat-tiles">{stats}</div>
    <div class="info-cards">
      <div class="info-card wide">
        <div class="info-head"><span class="feature-icon">{ICON['users']}</span><h3>Coaches and captains</h3></div>
        {ul(["Each team has an adult coach who is the primary contact and helps keep team structure during league play. Because of high school soccer rules, coaches can be parents, graduated former players, and more.",
             "Each team elects at least two captains to lead the team, on the field and off it.",
             f"{SITE_NAME} works with the coach and captains all season to keep fields and players available."])}
      </div>
      <div class="info-card">
        <div class="info-head"><span class="feature-icon">{ICON['clock']}</span><h3>Fields and times</h3></div>
        {ul(["Two weekday games a week, between 4 and 9 p.m.",
             f"Referees and scheduling handled by {SITE_NAME}",
             "Game times set with coaches and referees around field availability",
             "Specific fields and dates announced soon"])}
      </div>
      <div class="info-card">
        <div class="info-head"><span class="feature-icon">{ICON['shield']}</span><h3>Dates and fees</h3></div>
        {ul([f"First season in {SEASON}, across {STATE}",
             f"Team pricing between {PRICE}",
             "Up to 30 players per team",
             "Strict league rules and full insurance for all play",
             "Official registration will be announced shortly"])}
      </div>
    </div>
  </div>
</section>
"""
    html += cta_banner(f"Registration for {SEASON} opens soon",
                       "Let us know you're interested and we'll reach out with divisions, dates and next steps before registration opens.",
                       f"mailto:{EMAIL}", EMAIL)
    html += footer()
    return html


write("programs.html", page_programs())


# =========================================================
# INTEREST FORM (register.html — filename kept so existing links still work)
# =========================================================
FAQ = [
    ("Is this the official registration?",
     f"Not yet. This form tells us you're interested. Official registration for {SEASON} opens soon, and we'll reach out to everyone who filled this in first."),
    ("Who can play?",
     f"High school boys and girls in {STATE}. Teams can keep their school squad together over the summer or build a roster of high school players from the same area, up to 30 players."),
    ("How do divisions work?",
     "Boys and girls each have Divisions 1, 2 and 3: top-level competition, competitive play for rising teams, and development. Our league coordinators work with every team to find the right fit, and each division is split into pools."),
    ("When is the season?",
     f"The first season is {SEASON}: five weeks of pool play from July into August, two weekday games a week between 4 and 9 p.m., then the {CUP_NAME} knockout bracket on the final weekend. Specific fields and dates will be announced soon."),
    ("What does it cost?",
     f"Team pricing is between {PRICE}. Every game has a referee, and all play is fully insured."),
    ("Who coaches the team?",
     "Each team has an adult coach who is the primary contact. Because of high school soccer rules, coaches can be parents, graduated former players, and more. Each team also elects at least two captains."),
    ("Can we talk it through first?",
     f"Yes. We're happy to set up a call or in-person meeting. Email {EMAIL} or call {PHONE_DISPLAY}."),
]


def faq_block(items):
    out = []
    for q, a in items:
        out.append(f"""<details class="faq-item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>""")
    return "\n      ".join(out)


INVOLVED_STEPS = [
    ("Reach out", "Fill in the form below, or get in touch, and we'll follow up."),
    ("Tell your captains", "Let the captains on your team know about the league."),
    ("Share their info", "If you can, send us your captains' contact information so we can reach them directly."),
]


def page_register():
    html = head("Interested in Participating?", f"Interested in the {LEAGUE_NAME}? Tell us about your high school team and we'll follow up before {SEASON} registration opens.")
    html += header("register.html")
    steps = "\n      ".join(
        f'<div class="step-card"><span class="step-num">{i}</span><h3>{t}</h3><p>{d}</p></div>'
        for i, (t, d) in enumerate(INVOLVED_STEPS, 1))
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">Get Involved</p>
    <h1>{CTA_LABEL}</h1>
    <p>Official registration for {SEASON} opens soon. Tell us about your team and we'll take a look and follow up with divisions, dates and next steps.</p>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="steps grid-3">
      {steps}
    </div>
  </div>
</section>

<section class="section-flush">
  <div class="container narrow">
    <form class="contact-form card-form" action="{FORM_ENDPOINT}" method="POST">
{form_hidden(f"New {LEAGUE_NAME} interest form")}      <div class="form-grid">
        <div>
          <label for="name">Your name <span class="req">*</span></label>
          <input id="name" name="Name" type="text" required autocomplete="name">
        </div>
        <div>
          <label for="role">Your role <span class="req">*</span></label>
          <select id="role" name="Role" required>
            <option value="">Choose one…</option>
            <option>Head coach</option>
            <option>Assistant coach</option>
            <option>Team captain</option>
            <option>Player</option>
            <option>Parent / guardian</option>
            <option>Athletic director</option>
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
        <div>
          <label for="team">School or team name <span class="req">*</span></label>
          <input id="team" name="School or team" type="text" required autocomplete="organization">
        </div>
        <div>
          <label for="town">Town</label>
          <input id="town" name="Town" type="text" placeholder="Where your team is based">
        </div>
        <div>
          <label for="side">Boys or girls <span class="req">*</span></label>
          <select id="side" name="Boys or girls" required>
            <option value="">Choose one…</option>
            <option>Boys</option>
            <option>Girls</option>
            <option>Both</option>
          </select>
        </div>
        <div>
          <label for="division">Division you're thinking of</label>
          <select id="division" name="Division">
            <option>Not sure yet, help us decide</option>
            <option>Division 1: top-level competition</option>
            <option>Division 2: competitive play for rising teams</option>
            <option>Division 3: development and building experience</option>
          </select>
        </div>
        <div>
          <label for="roster">Approximate number of players</label>
          <input id="roster" name="Roster size" type="number" min="1" max="30" placeholder="Up to 30">
        </div>
        <div>
          <label for="call">Want a call or meeting?</label>
          <select id="call" name="Walkthrough">
            <option>No, email is fine</option>
            <option>Yes, a phone or video call</option>
            <option>Yes, an in-person meeting</option>
          </select>
        </div>
        <div class="full">
          <label for="captains">Captains' names and contact info</label>
          <textarea id="captains" name="Captains" class="short" placeholder="If you can, list your captains with an email or phone number so we can reach them directly."></textarea>
        </div>
        <div class="full">
          <label for="message">Anything else we should know?</label>
          <textarea id="message" name="Notes" class="short" placeholder="Questions, scheduling constraints, field access, how strong your team is…"></textarea>
        </div>
        <div class="full">
          <button type="submit" class="btn btn-primary btn-lg">Send My Info</button>
          <p class="form-note">This isn't a commitment. We'll reply to the email above. Questions first? Call <a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
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
      <h2>Common questions</h2>
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
    html = head("Thanks", f"Your message has been received by {SITE_NAME}.")
    html += header("")
    html += f"""
<section class="page-hero tall">
  <div class="container">
    <div class="check-mark">{ICON['trophy']}</div>
    <h1>Got it &mdash; thank you.</h1>
    <p>Your info is on its way to our inbox. We'll take a look and reply within a couple of days.</p>
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
# (number, filter category, tag css class, tag label, caption)
GALLERY_ITEMS = [
    (16, "boys", "boys", "Boys", "Taking on a defender"),
    (17, "boys", "boys", "Boys", "Captain's armband on for the throw-in"),
    (15, "matchday", "cup", "Matchday", "Senior night under the lights"),
    (18, "boys", "boys", "Boys", "Pushing the ball up the field"),
    (14, "founders", "coaches", "Founders", "Andrew with his leadership award"),
    (13, "founders", "coaches", "Founders", "Family day on the field at St. John's"),
    (1, "boys", "boys", "Boys", "Lining up a shot on goal"),
    (3, "girls", "girls", "Girls", "Girls' soccer in full stride"),
    (2, "boys", "boys", "Boys", "Team huddle before kickoff"),
    (5, "girls", "girls", "Girls", "A throw-in from the sideline"),
    (4, "boys", "boys", "Boys", "Racing for the ball down the wing"),
    (6, "boys", "boys", "Boys", "A squad ready for the season"),
    (7, "boys", "boys", "Boys", "Striking a first-time shot"),
    (8, "matchday", "cup", "Matchday", "Ready for kickoff"),
    (9, "matchday", "cup", "Matchday", "A hard-fought challenge at midfield"),
    (10, "matchday", "cup", "Matchday", "Chasing the game in open space"),
    (11, "boys", "boys", "Boys", "Team talk before the whistle"),
    (12, "matchday", "cup", "Matchday", "Wide open play across the pitch"),
]


def gallery_item(n, category, tagcls, label, caption):
    return f"""<figure class="gallery-item" data-category="{category}">
      <img src="images/gallery/gallery-{n}.jpg" alt="{caption}" loading="lazy">
      <span class="tag tag-{tagcls}">{label}</span>
      <figcaption class="gallery-cap">{caption}</figcaption>
    </figure>"""


def page_photos():
    html = head("Photos", f"Photos of high school boys' and girls' soccer from {SITE_NAME} and the {LEAGUE_NAME}.")
    html += header("photos.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">Gallery</p>
    <h1>On the Field</h1>
    <p>High school soccer across the boys' and girls' game, plus a look back at where our founders started.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="filter-bar">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="boys">Boys</button>
      <button class="filter-btn" data-filter="girls">Girls</button>
      <button class="filter-btn" data-filter="matchday">Matchday</button>
      <button class="filter-btn" data-filter="founders">Founders</button>
    </div>
    <div class="gallery-grid">
      {"".join(gallery_item(*item) for item in GALLERY_ITEMS)}
    </div>
    <p class="center fine-print">League photos, including the {CUP_NAME}, will be added once the first season kicks off in {SEASON}.</p>
  </div>
</section>
{lightbox()}
"""
    html += footer()
    return html


write("photos.html", page_photos())


# =========================================================
# NEWS (coming soon)
# =========================================================
def page_blog():
    html = head("News", f"News and updates from the {LEAGUE_NAME}, coming soon.")
    html += header("blog.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">News</p>
    <h1>League News</h1>
    <p>Registration updates, schedules and results from the {LEAGUE_NAME}.</p>
  </div>
</section>

<section>
  <div class="container narrow">
    <div class="coming-soon">
      <div class="feature-icon">{ICON['calendar']}</div>
      <p class="eyebrow">Coming Soon</p>
      <h2>News is on the way</h2>
      <p>We'll post registration updates, field announcements, schedules and results here as {SEASON} gets closer. For now, follow along on Instagram.</p>
      <div class="cta-actions">
        <a href="{INSTAGRAM_URL}" class="btn btn-primary" target="_blank" rel="noopener">Follow @{INSTAGRAM_HANDLE}</a>
        <a href="register.html" class="btn btn-navy">{CTA_LABEL}</a>
      </div>
    </div>
  </div>
</section>
"""
    html += footer()
    return html


write("blog.html", page_blog())


# =========================================================
# CONTACT
# =========================================================
def page_contact():
    html = head("Contact", f"Contact {SITE_NAME}: email {EMAIL} or call {PHONE_DISPLAY}.")
    html += header("contact.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">Contact</p>
    <h1>Get In Touch</h1>
    <p>Questions about divisions, coaching, refereeing or sponsorship? We're happy to talk, and we can set up a call or in-person meeting.</p>
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
          <span class="ic">{ICON['instagram']}</span>
          <div><strong>Instagram</strong><a href="{INSTAGRAM_URL}" target="_blank" rel="noopener">@{INSTAGRAM_HANDLE}</a></div>
        </div>
        <div class="contact-row">
          <span class="ic">{ICON['clock']}</span>
          <div><strong>First season</strong><span>{SEASON} &middot; {STATE}</span></div>
        </div>
        <div class="contact-row">
          <span class="ic">{ICON['trophy']}</span>
          <div><strong>{CTA_LABEL}</strong><a href="register.html">Fill out the interest form &rarr;</a></div>
        </div>
      </aside>

      <div>
        <h2>Send a Message</h2>
        <form class="contact-form" action="{FORM_ENDPOINT}" method="POST">
{form_hidden(f"New {SITE_NAME} website message")}          <div class="form-grid">
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
                <option>Joining the league</option>
                <option>Setting up a call or meeting</option>
                <option>Coaching</option>
                <option>Refereeing</option>
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
# MERCH
# =========================================================
def page_merch():
    html = head("Merch", f"{SITE_NAME} team merch and custom jerseys, coming soon.")
    html += header("merch.html")
    html += f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb">Shop</p>
    <h1>Team Merch &amp; Jerseys</h1>
    <p>Custom {SITE_NAME} jerseys for your squad. Order forms open soon.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div class="merch-card">
        <img src="images/merch-jersey.png" alt="Mock-up of a navy and blue {SITE_NAME} custom soccer jersey, front and back, with a sample player name and number" loading="lazy">
      </div>
      <div>
        <p class="eyebrow">Coming Soon</p>
        <h2>Custom jerseys, made for your team</h2>
        <p>We're setting up an online shop where every {LEAGUE_NAME} team can order custom {SITE_NAME} jerseys: your team name, your colors, and your players' names and numbers, shipped straight to your door.</p>
        <p>The shop isn't live yet, but it's coming before the season kicks off. Tell us you're interested or get in touch and we'll let you know the moment ordering opens.</p>
        <div class="hero-actions">
          <a href="register.html" class="btn btn-primary">{CTA_LABEL}</a>
          <a href="contact.html" class="btn btn-navy">Get Notified</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="center stack">
      <p class="eyebrow">What's Coming</p>
      <h2>Built for teams, not just fans</h2>
    </div>
    <div class="grid grid-3">
      <div class="feature">
        <div class="feature-icon">{ICON['shield']}</div>
        <div><h3>Custom Team Jerseys</h3><p>Your team name and colors on a real match-ready jersey.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['users']}</div>
        <div><h3>Names &amp; Numbers</h3><p>Personalize every jersey on the roster, player by player.</p></div>
      </div>
      <div class="feature">
        <div class="feature-icon">{ICON['bolt']}</div>
        <div><h3>Ordered Online</h3><p>Simple online ordering, shipped directly to your team.</p></div>
      </div>
    </div>
  </div>
</section>
"""
    html += cta_banner("Want first access when the shop opens?",
                       "Tell us about your team or send us a message and we'll reach out the moment jersey ordering goes live.",
                       "contact.html", "Contact Us")
    html += footer()
    return html


write("merch.html", page_merch())


# =========================================================
# 404
# =========================================================
def page_404():
    html = head("Page Not Found", f"That page doesn't exist. Head back to {SITE_NAME}.")
    html += header("")
    html += f"""
<section class="page-hero tall">
  <div class="container">
    <p class="eyebrow light">404</p>
    <h1>Offside &mdash; that page doesn't exist.</h1>
    <p>The page you're after was moved, renamed, or never existed.</p>
    <div class="cta-actions center-actions">
      <a href="index.html" class="btn btn-white btn-lg">Back to Home</a>
      <a href="register.html" class="btn btn-ghost btn-lg">{CTA_LABEL}</a>
    </div>
  </div>
</section>
"""
    html += footer()
    return html


write("404.html", page_404())

print("\nAll pages built.")
