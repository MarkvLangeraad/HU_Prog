def seizoen():
    maandnummer = eval(input('Welke maand is het (hier kunnen alleen getallen ingevuld worden)?'))
    if maandnummer >=3 and maandnummer <=5:
        print('Het is lente')
    elif maandnummer >=9 and maandnummer <=11:
        print('Het is herfst')
    else:
        print('Het is geen lente en ook geen herfst.')

seizoen()
