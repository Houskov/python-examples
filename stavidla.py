def generujStavidla(aktualniCislo, aktualniKombinace, hloubka, pocetPozic, pocetStavidel):
    if (hloubka < pocetStavidel):
        if aktualniCislo > 1:
            generujStavidla(aktualniCislo - 1, aktualniKombinace + " " + str(aktualniCislo - 1), hloubka + 1, pocetPozic, pocetStavidel)
        generujStavidla(aktualniCislo , aktualniKombinace + " " + str(aktualniCislo), hloubka + 1, pocetPozic, pocetStavidel)
        if aktualniCislo < pocetPozic:
            generujStavidla(aktualniCislo + 1, aktualniKombinace + " " + str(aktualniCislo + 1), hloubka + 1, pocetPozic, pocetStavidel)
    else:
        global celkem
        celkem = celkem + 1
        print(aktualniKombinace)

pocetStavidel = int(input())
pocetPozic = int(input())
celkem = 0
for i in range(pocetPozic):
    generujStavidla(i + 1, str(i + 1), 1, pocetPozic, pocetStavidel)
print("celkem" + " " + str(celkem))