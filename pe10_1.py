green = {'Weert', 'Heeze', 'Geldrop', 'Beukenlaan', 'Best', 'Boxtel'}
brown = {'Deurne', 'Helmond brouwershuis', 'Helmond', "Helmond 't hout", 'Best', 'Boxtel'}
green_brown = brown.intersection(green)
dif_brown_green = brown.difference(green)
union_brown_green = green.union(brown)

print(green)
print(brown)
print(green_brown)
print(dif_brown_green)
print(union_brown_green)
