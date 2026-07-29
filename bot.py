import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

mensaje = """🤖 El bot de GitHub funciona correctamente.

A partir de ahora empezaremos a buscar billetes Barcelona → Madrid.
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": mensaje
})

print("Mensaje enviado")
