from dates import generate_trip_dates
from telegram_bot import send_message

def main():
    viajes = generate_trip_dates()

    mensaje = "🚄 Buscando ofertas Barcelona → Madrid\n\n"

    mensaje += f"Viajes a comprobar: {len(viajes)}\n\n"

    mensaje += "Primeros viajes:\n"

    for viaje in viajes[:5]:
        mensaje += (
            f"{viaje['outbound']} ➜ {viaje['inbound']}\n"
        )

    send_message(mensaje)


if __name__ == "__main__":
    main()
