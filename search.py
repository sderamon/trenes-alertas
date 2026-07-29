from random import randint


def buscar_ofertas(viajes):
    """
    Devuelve ofertas simuladas para comprobar
    que el bot funciona.
    """

    ofertas = []

    for viaje in viajes[:10]:

        precio_ida = randint(7, 20)
        precio_vuelta = randint(7, 20)

        total = precio_ida + precio_vuelta

        if total <= 30:

            ofertas.append({
                "ida": viaje["outbound"],
                "vuelta": viaje["inbound"],
                "precio_ida": precio_ida,
                "precio_vuelta": precio_vuelta,
                "total": total,
                "operador": "PRUEBA"
            })

    return ofertas
