Stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def read_beginstation(stations):
    while True:
        Start = input('Enter a startingstation: ')
        if Start not in stations:
            print('Enter a valid station')
        else:
            break
    return Start

def read_endstation(stations, begin):
    while True:
        End = input('Enter endstation: ')
        if End not in stations or stations.index(End) < stations.index(begin):
            print('Enter a valid station')
        else:
            break
    return End

def broadcasters_trip(stations, beginstation, endstation):
    starting_index = stations.index(beginstation) + 1
    print('The beginstation', beginstation, 'is the', stations.index(beginstation), 'th station in the traject.')
    print('The endstation', endstation, 'is the', stations.index(endstation), 'th station in the traject.')
    print('The distance is', stations.index(endstation) - stations.index(beginstation), 'station(s).')
    print('The price of a ticket', 5 * (stations.index(endstation) - stations.index(beginstation)), 'euro.')
    print(' ')
    print('You entered the train at: ', beginstation, '-', stations[starting_index])
    print(' ')
    print('You leave the train at: ', endstation)

beginstation = read_beginstation(Stations)
endstation = read_endstation(Stations, beginstation)
broadcasters_trip(Stations, beginstation, endstation)
