def vyhodnotVyraz(vyraz):
    mezivysledek = 0
    posledniCislo = ""
    posledniZnamenko = "+"
    for i in range(len(vyraz)):
        if (vyraz[i]!="+" and vyraz[i]!="-"):
            posledniCislo = posledniCislo + vyraz[i]
        else:
            if (posledniZnamenko == "+"):
                mezivysledek += int(posledniCislo)
                posledniCislo = ""
                posledniZnamenko = vyraz[i]
            elif (posledniZnamenko == "-"):
                mezivysledek = mezivysledek - int(posledniCislo)
                posledniCislo = ""
                posledniZnamenko = vyraz[i]
    if (posledniZnamenko == "+"):
        mezivysledek += int(posledniCislo)
    else:
        mezivysledek -= int(posledniCislo)
    return mezivysledek

def generujVyraz(aktualniCislo, aktualniVyraz, n):
    if aktualniCislo <= 9:
        generujVyraz(aktualniCislo + 1, aktualniVyraz + str(aktualniCislo), n)
        generujVyraz(aktualniCislo + 1, aktualniVyraz + "+" + str(aktualniCislo), n)
        generujVyraz(aktualniCislo + 1, aktualniVyraz + "-" + str(aktualniCislo), n)
    else:
        if(vyhodnotVyraz(aktualniVyraz) == n):
            print(aktualniVyraz)


n = int(input())
generujVyraz(2, "1", n)