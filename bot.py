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

    # ORIGEN
    inputs.nth(0).fill("Barcelona")
    page.wait_for_timeout(1000)
    page.get_by_role("option").first.click()

    # DESTINO
    inputs.nth(1).fill("Madrid")
    page.wait_for_timeout(1000)
    page.get_by_role("option").first.click()

    # Abrir calendario
    inputs.nth(2).click()
    page.wait_for_timeout(3000)

    print("\nTODAS LAS CLASES DEL CALENDARIO\n")

    elementos = page.locator("[class]")

    for i in range(elementos.count()):
        try:
            clase = elementos.nth(i).get_attribute("class")
            texto = elementos.nth(i).inner_text().strip()

            if "€" in texto:
                print("--------------------")
                print(clase)
                print(texto)

        except:
            pass

    page.screenshot(path="ventas.png", full_page=True)

    browser.close()
