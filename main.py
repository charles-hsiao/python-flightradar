import airlines as air


def main():

    airlines = air.get_all_airlines()
    for item in airlines:
        airline_code = item['ICAO']
        flights = air.get_airline_flights(airline_code)
        print(flights)

    # CPA=Cathay Pacific
    #flights = air.get_airline_flights('CPA')
    #print(flights)

    # Get all airports
    #airports = air.get_all_airports()
    #print(airports)


if __name__ == '__main__':
    main()
