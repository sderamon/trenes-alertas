from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(viewport={"width": 1440, "height": 1200})

    page.goto(
        "https://ventas.ouigo.com/es-ES",
        wait_until="networkidle",
        timeout=120000
    )

    print("\nINPUTS\n")

    inputs = page.locator("input")

    for i in range(inputs.count()):
        inp = inputs.nth(i)
        print(
            i,
            inp.get_attribute("placeholder"),
            inp.get_attribute("aria-label"),
            inp.get_attribute("type"),
        )

    browser.close()
