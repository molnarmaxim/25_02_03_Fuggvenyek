'''
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!

'''

def paros_e(list):
    for x in list:
        if x % 2 == 0:
            return True

szamok = [1, 3, 5, 2, 4, 10]
print("Van páros?", paros_e(szamok))