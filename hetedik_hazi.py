szamok = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]

def binaris_kereses():
    also = 0
    felso = len(szamok)
    lepes = 0
    talalat = True
    while also <= felso:
        lepes += 1
        kozep = (also+felso)//2
        if szamok[kozep]>70:
            felso = kozep-1

        elif szamok[kozep]<70:
            also = kozep+1
        elif szamok[kozep] == 70:
            hely = kozep
            break
    else:
        talalat = False

    if talalat==True:
        print("lépés:",lepes)
        print("also érték:", also)
        print("felső érték:", felso)
        print("k érték", hely)

    else:
        print("Nincs találat")


if __name__  ==  "__main__" :
    binaris_kereses()