def forditas(beker):
    szo = beker
    modosit =""
    betuk="szzsnytygyly"
    feltetel=True
    for z in range(0,len(szo)):
        if z != (len(szo)-1) and szo[z]+szo[z+1] in betuk and feltetel==True:
            modosit+=szo[z+1]+szo[z]
            feltetel=False

        elif feltetel==True:
            modosit+=szo[z]

        else:
            feltetel = True
    return modosit



def palindrom():
    a = "arany nyara"
    darabol = a.split()
    szo = ""
    for x in range(0, len(darabol)):
        szo+=darabol[x]
    duplabetu_forditas=forditas(szo)
    forditott_szo = duplabetu_forditas[::-1]
    if szo==forditott_szo:
        print(a, "palindróm")
    else:
        print(a, "nem palindróm")

if __name__ == "__main__":
    palindrom()
