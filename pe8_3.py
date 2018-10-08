invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
x = invoer.split('-')
print(x)
a= max(invoer)
b= min (x)
c= len(x)
d=0
for getal in x:
    d = d + int(getal)
e= d/c
print ('grootste getal is ',a, 'kleinste getal',b)
print ('Aantal getallen: ',c, 'Som van de getallen: ',d)
print ('Gemiddelde: ', e)
