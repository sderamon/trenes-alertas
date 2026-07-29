import os
import requests


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def enviar_mensaje(texto):
    """Envía un mensaje a Telegram."""

    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Faltan TELEGRAM_TOKEN o CHAT_ID")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    datos = {
        "chat_id": CHAT_ID,
        "text": texto
    }

    r = requests.post(url, data=datos, timeout=30)

    print("Telegram:", r.status_code)
