def convert(Temperatuur):
    f = (Temperatuur*1.8) +32
    return f


def tabel():
    print('{:>3}{:>6}'.format('F', 'C'))
    for f in range(-30,50,10):
        print('{:>3}{:>6}'.format(round(convert(f), 2 ), round(float(f), 2)))
tabel()



