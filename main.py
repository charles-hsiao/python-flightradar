import airlines as air


def main():
    #airlines = air.get_all_airlines()
    #print(airlines)

    # CPA=Cathay Pacific
    flights = air.get_airline_flights('CPA')
    print(flights)


if __name__ == '__main__':
    main()
