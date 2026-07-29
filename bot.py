from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(viewport={"width": 1440, "height": 1200})

    page.goto(
        "https://www.ouigo.com/es",
        wait_until="domcontentloaded",
        timeout=120000
    )

    page.wait_for_timeout(10000)

    print(page.title())
    print(page.url)

   

    botones = page.locator("button").all_inner_texts()

    print("BOTONES:")
    for b in botones:
        print("-", b)

    browser.close()
