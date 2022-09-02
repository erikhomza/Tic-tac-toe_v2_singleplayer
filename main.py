import random
jkl = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
hrac_1_vytazstva = 0
hrac_2_vytazstva = 0
hra = True



def nova_hra():
    global jkl
    global hra
    print("Keď chceš hrať znova napíš 1 inak napíš 0.")
    restart = input()
    if restart == "1":
        jkl = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        hra = True
        piskorky()
    elif restart == "0":
        quit()
    else:
        nova_hra()


def kontrola1():
    global hra
    global jkl
    global hrac_1_vytazstva
    global hrac_2_vytazstva
    if jkl[0][0] == "x" and jkl[0][1] == "x" and jkl[0][2] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[1][0] == "x" and jkl[1][1] == "x" and jkl[1][2] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[2][0] == "x" and jkl[2][1] == "x" and jkl[2][2] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][0] == "x" and jkl[1][0] == "x" and jkl[2][0] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][1] == "x" and jkl[1][1] == "x" and jkl[2][1] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][2] == "x" and jkl[1][2] == "x" and jkl[2][2] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][0] == "x" and jkl[1][1] == "x" and jkl[2][2] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][2] == "x" and jkl[1][1] == "x" and jkl[2][0] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    else:
        pass


def kontrola2():
    global jkl
    global hra
    global hrac_1_vytazstva
    global hrac_2_vytazstva
    if jkl[0][0] == "O" and jkl[0][1] == "O" and jkl[0][2] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[1][0] == "O" and jkl[1][1] == "O" and jkl[1][2] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[2][0] == "O" and jkl[2][1] == "O" and jkl[2][2] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][0] == "O" and jkl[1][0] == "O" and jkl[2][0] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][1] == "O" and jkl[1][1] == "O" and jkl[2][1] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][2] == "O" and jkl[1][2] == "O" and jkl[2][2] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][0] == "O" and jkl[1][1] == "O" and jkl[2][2] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0][2] == "O" and jkl[1][1] == "O" and jkl[2][0] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    else:
        pass

def hracia_plocha(jkl):
    print(" ", "0", "1", "2")
    print("0", jkl[0][0], jkl[0][1], jkl[0][2])
    print("1", jkl[1][0], jkl[1][1], jkl[1][2])
    print("2", jkl[2][0], jkl[2][1], jkl[2][2])

def hrac1():
    print("Na rade je hráč 1.")
    print("Napíš číslo riadku od 0 po 2.")
    riadok = input()
    print("Napíš číslo stĺpca od 0 po 2.")
    stlpec = input()
    if riadok == "0" or riadok == "1" or riadok == "2":
        if stlpec == "0" or stlpec == "1" or stlpec == "2":
            if jkl[int(riadok)][int(stlpec)] == "-":
                jkl[int(riadok)][int(stlpec)] = "x"
            else:
                print("Chybný ťah.")
                hrac1()
        else:
            print("Chybný ťah.")
            hrac1()
    else:
        print("Chybný ťah.")
        hrac1()

def hrac2():
    riadok = random.randint(0, 2)
    stlpec = random.randint(0, 2)
    if riadok == 0 or riadok == 1 or riadok == 2:
        if stlpec == 0 or stlpec == 1 or stlpec == 2:
            if jkl[int(riadok)][int(stlpec)] == "-":
                jkl[int(riadok)][int(stlpec)] = "O"
            else:
                hrac2()
        else:
            hrac2()
    else:
        hrac2()

def piskorky():
    global hra
    global jkl
    hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
        print("Na rade je hráč 2.")
    if hra:
        hrac2()
        kontrola2()
        hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
        print("Na rade je hráč 2.")
    if hra:
        hrac2()
        kontrola2()
        hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
        print("Na rade je hráč 2.")
    if hra:
        hrac2()
        kontrola2()
        hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
        print("Na rade je hráč 2.")
    if hra:
        hrac2()
        kontrola2()
        hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
    if hra:
        print("Remíza.")
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        nova_hra()
piskorky()