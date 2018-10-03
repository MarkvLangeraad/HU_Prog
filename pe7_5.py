def gemiddelde():
    zin = input('Vul hier je zin in:')
    woorden_list = zin.split()
    gemiddelde_lengte_woord = sum(len(woord) for woord in woorden_list) / len(woorden_list)
    print('Je zin heeft een gemiddelde van',gemiddelde_lengte_woord, 'letter(s) per woord.')

gemiddelde()
