import flightradar24


def get_all_airlines():
    fr = flightradar24.Api()
    airlines = fr.get_airlines()
    return airlines['rows']


def get_airline_flights(airline_code):
    fr = flightradar24.Api()
    flights_data = fr.get_flights(airline_code)
    flights = []

    for key, value in flights_data.items():
        if isinstance(value, list):
            flight_dict = {"airline": airline_code, "from": value[11], "to": value[12], "aircraft": value[8]}
            flights.append(flight_dict)

    return flights


def get_all_airports():
    fr = flightradar24.Api()
    airports = fr.get_airports()
    return airports['rows']

