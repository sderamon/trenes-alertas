from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        viewport={"width": 1440, "height": 1200}
    )

    page.goto(
        "https://ventas.ouigo.com/es-ES",
        wait_until="domcontentloaded",
        timeout=120000
    )

    page.wait_for_timeout(8000)

    page.screenshot(path="ventas.png", full_page=True)

    print(page.title())
    print(page.url)

    print("\nTEXTBOXES\n")

    for i, e in enumerate(page.get_by_role("textbox").all()):
        print(i)

    print("\nCOMBOBOX\n")

    for i, e in enumerate(page.get_by_role("combobox").all()):
        print(i)

    print("\nBOTONES\n")

    for t in page.locator("button").all_inner_texts():
        print("-", t)

    browser.close()
