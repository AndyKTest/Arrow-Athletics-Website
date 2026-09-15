import sys
from playwright.sync_api import sync_playwright

pages = sys.argv[1:] or ["index.html", "about.html", "programs.html", "register.html",
                         "photos.html", "blog.html", "contact.html", "thanks.html",
                         "blog-registration-open.html"]

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    ctx = b.new_context(viewport={"width": 1400, "height": 1000})
    for name in pages:
        pg = ctx.new_page()
        pg.goto(f"http://localhost:8765/{name}", wait_until="load")
        # loading="lazy" is right for the live site but races a full-page capture,
        # so force every image to load and settle before screenshotting
        pg.evaluate("""async () => {
            const imgs = [...document.images];
            imgs.forEach(i => { i.loading = 'eager'; if (!i.complete) i.src = i.src; });
            await Promise.all(imgs.map(i => i.complete ? null : new Promise(r => {
                i.addEventListener('load', r, {once: true});
                i.addEventListener('error', r, {once: true});
            })));
        }""")
        pg.wait_for_timeout(400)
        pg.screenshot(path=f"/tmp/s-{name}.png", full_page=True)
        print("shot", name)
        pg.close()

    m = b.new_context(viewport={"width": 390, "height": 844})
    mp = m.new_page()
    mp.goto("http://localhost:8765/index.html", wait_until="load")
    mp.wait_for_timeout(300)
    mp.screenshot(path="/tmp/s-mobile.png", full_page=True)
    mp.click(".nav-toggle")
    mp.wait_for_timeout(250)
    mp.screenshot(path="/tmp/s-mobile-nav.png")
    mp2 = m.new_page()
    mp2.goto("http://localhost:8765/register.html", wait_until="load")
    mp2.wait_for_timeout(300)
    mp2.screenshot(path="/tmp/s-mobile-register.png", full_page=True)
    print("shot mobile")
    b.close()
