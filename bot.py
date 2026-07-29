from dates import generate_trip_dates
from search import buscar_ofertas
from telegram_bot import send_message


def main():

    viajes = generate_trip_dates()

    ofertas = buscar_ofertas(viajes)

    if not ofertas:
        print("No hay ofertas")
        return

    mensaje = "🚄 OFERTAS ENCONTRADAS\n\n"

    for oferta in ofertas:

        mensaje += (
            f"📅 {oferta['ida']} → {oferta['vuelta']}\n"
            f"💶 {oferta['precio_ida']} € + {oferta['precio_vuelta']} €"
            f" = {oferta['total']} €\n"
            f"🚅 {oferta['operador']}\n\n"
        )

    send_message(mensaje)


if __name__ == "__main__":
    main()
