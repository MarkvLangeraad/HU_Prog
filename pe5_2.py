Naam= input('Wat is uw naam?')
Leeftijd= eval(input('Wat is uw leeftijd?'))
Paspoort= input('Heeft u een Nederlands paspoort?')


if Leeftijd  >= 18 and Paspoort == 'ja' or Paspoort== 'Ja' : print(Naam + ' '+ 'gefeliciteerd je mag stemmen.')


else :print(Naam+ ', sorry je mag niet stemmen.')
