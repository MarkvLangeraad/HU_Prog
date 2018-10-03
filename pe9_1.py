def sum():
    total=0
    while True:
        getal = eval(input('Volgende getal:'))
        if getal== 0:
            break
        total += getal

    print('Dit is de uitkomst van de optelling', total)
sum()
