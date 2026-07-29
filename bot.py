from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(viewport={"width": 1440, "height": 1200})

    page.goto(
        "https://ventas.ouigo.com/es-ES",
        wait_until="networkidle",
        timeout=120000
    )

    inputs = page.locator("input")

    # Origen
    inputs.nth(0).fill("Barcelona Sants")

    # Destino
    inputs.nth(1).fill("Madrid")

    page.wait_for_timeout(3000)

    page.screenshot(path="ventas.png", full_page=True)

    browser.close()
