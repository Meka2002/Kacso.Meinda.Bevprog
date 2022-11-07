atlag = 0

with open("be_ketto.txt", "r",) as f:
    osszeg = 0
    darab = 0

    sor = f.readline()

    while sor:
        osszeg += int(sor)
        darab+=1
        sor = f.readline()

atlag = osszeg / darab

with open("ki.txt", "w") as f:
    f.write("Az átlag:" +str(atlag) + "\n")