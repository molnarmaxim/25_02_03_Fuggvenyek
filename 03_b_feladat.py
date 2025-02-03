'''
Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)
'''
running = True
szamok = []
while running:
    hozzaad = int(input("Kérlek adj meg egy számot a listába: "))
    if hozzaad < 0:
        running = False
    else: 
        szamok.append(hozzaad)

def harommal_oszthatok(list):
    oszthatok = []
    for x in list:
        if x % 3 == 0:
            oszthatok.append(x)
    print(oszthatok)

harommal_oszthatok(szamok)