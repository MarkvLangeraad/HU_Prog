Naam=input('Wat is de naam van de hardloper?')


def time():
    import datetime
    vandaag = datetime.datetime.today()
    datum = vandaag.strftime('%a %d %b %y ')
    tijd = vandaag.strftime('%X')

    with open('/Users/Mark van Langeraad/Desktop/hardlopers.txt', 'a') as f:
     f.write('{}, {}, {}\n'.format(datum, tijd, Naam))
     print('{} , {}, {} Saved. '.format(datum, tijd, Naam))

    f.close()

time()
