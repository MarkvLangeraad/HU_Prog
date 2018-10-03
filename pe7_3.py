def tel():
    lijst= []
    with open('/users/Mark van Langeraad/Desktop/kaartnummers.txt', 'r') as f:
        zin= f.readlines()
        aantal_zinnen=len(zin)
        strip= [f.strip()for f in zin]

        print('Dit bestand bestaat uit {} regels.'.format(aantal_zinnen))

        for x in strip:
            gesplit= x.split(',')
            lijst.append(gesplit)
        kaartnummer= max(lijst)
        regel = lijst.index(kaartnummer)

        print('Het grootste kaartnummer binnen dit bestand is: {}, en dat getal staat op regel {}.'.format(kaartnummer[0], regel + 1 ))

    f.close()

tel()


