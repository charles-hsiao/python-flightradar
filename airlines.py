from lxml import html
import requests
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


def get_aircraft(model):
    # WTC: https://www.skybrary.aero/index.php/ICAO_Wake_Turbulence_Category
    # - H (Heavy) aircraft types of 136 000 kg (300 000 lb) or more;
    # - M (Medium) aircraft types less than 136 000 kg (300 000 lb) and more than 7 000 kg (15 500 lb); and
    # - L (Light) aircraft types of 7 000 kg (15 500 lb) or less.
    # - Super Heavy for Airbus A380-800 with a maximum take-off mass in the order of 560 000 kg. (see Airbus A380 Wake Vortex Guidance)

    # APC: https://www.skybrary.aero/index.php/Aircraft_Approach_Category_(APC)
    # Category
    # - A: Speed 90 knots or less.
    # - B: Between 91 and 120 knots.
    # - C: Between 121 and 140 knots.
    # - D: Between 141 knots and 165 knots.
    # - E: Speed 166 knots or more. Only assigned to certain Military Aircraft.

    res = requests.get('https://www.skybrary.aero/index.php/' + model)
    tree = html.fromstring(res.text)
    arr = tree.xpath('//*[@id="mw-content-text"]/table[1]//text()')

    strip_list = []
    for value in arr:
        string_value = value.strip()
        if string_value != '':
            strip_list.append(string_value)

    result_dict = {}
    if 'Name' in strip_list and 'Manufacturer' in strip_list and 'WTC' in strip_list and 'APC' in strip_list:
        index_name = strip_list.index('Name') + 1
        index_manufacturer = strip_list.index('Manufacturer') + 1
        index_wtc = strip_list.index('WTC') + 1
        index_apc = strip_list.index('APC') + 1

        result_dict = {
            'name': strip_list[index_name],
            'manufacturer': strip_list[index_manufacturer],
            'capacity': strip_list[index_wtc],
            'apc': strip_list[index_apc]
        }

    return result_dict

