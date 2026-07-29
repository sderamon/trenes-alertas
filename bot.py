from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(viewport={"width": 1440, "height": 1200})

    page.goto(
        "https://ventas.ouigo.com/es-ES",
        wait_until="networkidle",
        timeout=120000
    )

    # Escribir origen
    origen = page.locator("input").nth(0)
    origen.fill("Barcelona")

    page.wait_for_timeout(2000)

    # Mostrar las opciones que aparecen
    opciones = page.locator('[role="option"]')

    print("Opciones:", opciones.count())

    for i in range(opciones.count()):
        print(opciones.nth(i).inner_text())

    page.screenshot(path="ventas.png", full_page=True)

    browser.close()
