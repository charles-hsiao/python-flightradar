import json
import csv


def load_json(file_path):
    with open(file_path, encoding='utf-8') as data_file:
        data = json.load(data_file)
    return data


def process_airports(csv_file, airports_data, countries_data):
    continent_name_dict = {
        "AF": "Africa",
        "AN": "Antarctica",
        "AS": "Asia",
        "EU": "Europe",
        "NA": "North America",
        "OC": "Oceania",
        "SA": "South America"
    }
    country_code_dict = {}
    for country_data in countries_data:
        country_name = country_data['name']
        country_iso = country_data['alpha-2']
        country_code_dict[country_iso] = country_name

    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for airport in airports_data:
            airport_iata = airport['iata']
            airport_country_iso = airport['iso']
            if airport_country_iso in country_code_dict:
                airport_country = country_code_dict[airport_country_iso]
                airport_continent = airport['continent']
                if airport_continent in continent_name_dict:
                    airport_continent_name = continent_name_dict[airport_continent]
                    writer.writerow([airport_iata, airport_country_iso, airport_country, airport_continent, airport_continent_name])
                else:
                    print('Unable to find continent:' + airport_continent_name)
            else:
                print('Unable to find country_iso: ' + airport_country_iso)


airports_data_file = 'dataset/airports_data.json'
air_data = load_json(airports_data_file)

countries_data_file = 'dataset/countries_data.json'
countries_data = load_json(countries_data_file)

csv_output_file = 'airports.csv'
process_airports(csv_output_file, air_data, countries_data)

