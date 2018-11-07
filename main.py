import airlines as air

def main():
    #airlines = air.get_all_airlines()
    #print(len(airlines['rows']))
    #for item in airlines['rows']:
    #    airline_code = item['ICAO']
    #    print(airline_code)
        #flights = air.get_airline_flights(airline_code)
        #print(flights)

        #print(value)

    #print(airlines['rows'][0]['ICAO'])

    # CPA=Cathay Pacific
    #flights = air.get_airline_flights('CPA')
    #print(flights)

    # Get all airports
    airports = air.get_all_airports()
    print(len(airports['rows']))


if __name__ == '__main__':
    main()
