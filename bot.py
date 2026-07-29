from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(viewport={"width": 1440, "height": 1200})

    page.goto(
        "https://www.ouigo.com/es",
        wait_until="domcontentloaded",
        timeout=120000
    )

    page.wait_for_timeout(5000)

    print(page.title())
    print(page.url)

    print("\nINPUTS ENCONTRADOS:\n")

    for i, locator in enumerate(page.locator("input").all()):
        print(i, locator.get_attribute("type"), locator.get_attribute("placeholder"))

    print("\nTEXTBOX:\n")

    for i, locator in enumerate(page.get_by_role("textbox").all()):
        print(i)

    print("\nCOMBOBOX:\n")

    for i, locator in enumerate(page.get_by_role("combobox").all()):
        print(i)

    browser.close()
