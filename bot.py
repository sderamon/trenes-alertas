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
    inputs.nth(0).fill("Barcelona")
    page.wait_for_timeout(1000)
    page.get_by_role("option").first.click()

    # Destino
    inputs.nth(1).fill("Madrid")
    page.wait_for_timeout(1000)
    page.get_by_role("option").first.click()

    # Abrir calendario de ida
    inputs.nth(2).click()
    page.wait_for_timeout(2000)

    print("\nELEMENTOS CON EURO\n")
    
    for e in page.locator("*").all():
        try:
            txt = e.inner_text().strip()
            if "€" in txt:
                print("-----")
                print(txt)
            if len(txt) > 500:
                continue
        except:
            pass

    page.screenshot(path="ventas.png", full_page=True)

    browser.close()
