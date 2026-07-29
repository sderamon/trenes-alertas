from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page(
            viewport={"width": 1440, "height": 1200}
        )

        page.goto("https://www.ouigo.com/es", wait_until="networkidle")

        # Espera unos segundos por si aparece un banner de cookies
        page.wait_for_timeout(5000)

        page.screenshot(path="ouigo.png", full_page=True)

        print("Captura realizada")

        browser.close()


if __name__ == "__main__":
    main()
