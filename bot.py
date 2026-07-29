from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(viewport={"width": 1440, "height": 1200})

    page.goto(
        "https://ventas.ouigo.com/es-ES",
        wait_until="networkidle",
        timeout=120000
    )

    origen = page.locator("input").nth(0)
    origen.fill("Barcelona")

    page.wait_for_timeout(1500)

    # Seleccionar Barcelona - Sants
    page.get_by_role("option").first.click()

    page.wait_for_timeout(1000)

    destino = page.locator("input").nth(1)

    print("Destino deshabilitado:", destino.is_disabled())

    page.screenshot(path="ventas.png", full_page=True)

    browser.close()
