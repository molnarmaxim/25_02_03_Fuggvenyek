'''
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!
'''


def harommal_oszthatok(list):
    oszthatok = []
    for x in list:
        if x % 3 == 0:
            oszthatok.append(x)
    print(oszthatok)

szamok = [3, 6, 1, 2]
harommal_oszthatok(szamok)