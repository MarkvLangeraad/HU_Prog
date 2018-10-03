def standaardprijs(afstandKM):
    'Prijs van een kaartje op afstand'
    if afstand <=0:
        prijs_kaartje=0
    elif afstand >=50:
        prijs_kaartje=afstandKM*0.60 + 15
    else:
        prijs_kaartje=afstandKM*0.80
    return prijs_kaartje

afstand= eval(input('Hoeveel kilometer wilt u reizen?'))

res1= standaardprijs(afstand)
print('Dit is de standaard prijs:', res1, 'euro')

def ritprijs(leeftijd, weekend):
    'Leeftijd & Weekendrit & AfstandKM'
    if age > 12 and age <65 and weekend=='Ja' or weekend== 'ja':
        prijs2= res1
    elif age > 12 and age <65 and weekend== 'Nee' or weekend== 'nee':
        prijs2= res1 * 0.60
    if age <= 12 or age >= 65  and weekend== 'Ja' or weekend== 'ja':
        prijs2=res1 *0.65
    elif age >= 12 or age >= 65 and weekend== 'Nee' or weekend== 'nee':
        prijs2=res1 *0.70
    return prijs2

weekendendrit= input('Is het weekend?')
age= eval(input('Hoe oud bent u?'))

res2= ritprijs(age, weekendendrit)
print('€',res2, 'dit is de ritprijs')
print('Fijne reis!')

