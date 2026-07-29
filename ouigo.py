from playwright.sync_api import sync_playwright


class Ouigo:

    def __init__(self):
        self.p = None
        self.browser = None
        self.page = None

    def abrir(self):
        self.p = sync_playwright().start()

        self.browser = self.p.chromium.launch(
            headless=True
        )

        self.page = self.browser.new_page(
            viewport={"width": 1440, "height": 1200}
        )

        self.page.goto(
            "https://ventas.ouigo.com/es-ES",
            wait_until="networkidle",
            timeout=120000
        )

    def seleccionar_origen_destino(self):

        inputs = self.page.locator("input")

        # Origen
        inputs.nth(0).fill("Barcelona")
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("option").first.click()

        # Destino
        inputs.nth(1).fill("Madrid")
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("option").first.click()

    def abrir_calendario(self):

        inputs = self.page.locator("input")
        inputs.nth(2).click()

        self.page.wait_for_timeout(2000)

    def captura(self):
        self.page.screenshot(
            path="ventas.png",
            full_page=True
        )

    def cerrar(self):

        self.browser.close()
        self.p.stop()
