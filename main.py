import airlines as air
import csv


def main():
    
    csv_file_name = 'output.csv'
    aircraft_capacity_dict = {}
    counter = 0
    airlines = air.get_all_airlines()
    count_all_airlines = len(airlines)
    with open(csv_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for airline in airlines:
            counter += 1
            print('Start: ' + str(counter) + '/' + str(count_all_airlines))
            airline_code = airline['ICAO']
            flights = air.get_airline_flights(airline_code)
            if len(flights) > 0:
                for flight in flights:
                    data_airline = flight['airline']
                    data_from = flight['from']
                    data_to = flight['to']
                    data_aircraft = flight['aircraft']
                    if data_airline != '' and data_from != 0 and data_to != '' and data_aircraft != '':
                        # Reduce progressing time: If in aircraft_capacity_dict, no need to retrieve again
                        if data_aircraft in aircraft_capacity_dict:
                            data_capacity = aircraft_capacity_dict[data_aircraft]
                        else:
                            aircraft_arr = air.get_aircraft(data_aircraft)
                            if len(aircraft_arr) > 0:
                                data_capacity = aircraft_arr['capacity']
                                aircraft_capacity_dict[data_aircraft] = data_capacity
                            else:
                                data_capacity = False
                        if data_capacity:
                            print(data_airline, data_from, data_to, data_aircraft, data_capacity)
                            writer.writerow([data_airline, data_from, data_to, data_aircraft, data_capacity])
    
    #csv_file_name = 'nodes.csv'
    #airports = air.get_all_airports()
    #with open(csv_file_name, 'w', newline='') as csv_file:
    #    writer = csv.writer(csv_file)
    #    for airport_inf in airports:
    #        airport = airport_inf['iata']
    #        writer.writerow([airport, airport])

    # CPA=Cathay Pacific
    #flights = air.get_airline_flights('CPA')
    #print(flights)

    # Get all airports
    #airports = air.get_all_airports()
    #print(airports)

    # CRJ9, B77W, A333
    #model = 'B77W'
    #capacity = air.get_aircraft(model)
    #print(capacity)


if __name__ == '__main__':
    main()
