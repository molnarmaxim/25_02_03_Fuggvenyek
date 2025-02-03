'''
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
'''

def kerulet(x, *args):
    if not args:
        #Négyzet
        print(4*x)
    if len(args) == 1:
        a = x
        b = args[0]
        print(2*a + 2*b)
    if len(args) == 2:
        a = x
        b = args[0]
        c = args[1]
        print(a+b+c)
    oldalak = [x] + list(args)
    if len(oldalak) < 3

    
kerulet(4, 2)
