from datetime import date, timedelta
from config import SEARCH_DAYS, STAY_NIGHTS


def generate_trip_dates():
    """
    Genera viajes con estancia de STAY_NIGHTS
    durante los próximos SEARCH_DAYS.
    """

    today = date.today()

    trips = []

    for i in range(SEARCH_DAYS):
        outbound = today + timedelta(days=i)
        inbound = outbound + timedelta(days=STAY_NIGHTS)

        trips.append({
            "outbound": outbound,
            "inbound": inbound
        })

    return trips


if __name__ == "__main__":
    viajes = generate_trip_dates()

    for viaje in viajes[:10]:
        print(
            viaje["outbound"],
            "->",
            viaje["inbound"]
        )

    print(f"\nTotal viajes: {len(viajes)}")
