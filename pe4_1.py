cijferICOR= eval(input('Wat voor cijfer ga je halen voor ICOR?'))
cijferCSN= eval(input('Wat voor cijfer ga je halen voor CSN?'))
cijferPROG= eval(input('Wat voor cijfer ga je halen voor PROG?'))
gemiddeld_cijfer= (str((cijferPROG+cijferCSN+cijferICOR)/3))
print('Dit is je gemiddelde cijfer:'+ ' '+ gemiddeld_cijfer)

beloningICOR= (cijferICOR*30)
beloningCSN= (cijferCSN*30)
beloningPROG= (cijferPROG*30)
totale_beloning= (str(beloningCSN+beloningICOR+beloningPROG))
print('Dit is je totale beloning van de cursussen:'+ ' '+ totale_beloning)

print('Je gemiddelde cijfer:'+ gemiddeld_cijfer + ' '+ 'levert een bedrag op van'+ ' '+ '€'+ totale_beloning)
