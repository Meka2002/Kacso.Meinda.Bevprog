def beolvas():
    zenek = []
    with open ("playlist.txt", "r", encoding="utf8") as f:
        tartalom = f.readline()

        while tartalom:
            thisdict = {}
            thisdict["eloado"] = tartalom.split(";")[0]
            thisdict["cim"] = tartalom.split(";")[1]
            thisdict["mufaj"] = tartalom.split(";")[2]
            thisdict["hossz"] = int(tartalom.split(";")[3])
            zenek.append(thisdict)

            tartalom = f.readline()
    return zenek

def teljesz_hossz(zenek = beolvas()):
    osszeg = 0
    perc = 0
    masodperc = 0
    for i in range(0, len(zenek)):
        osszeg += zenek[i].get("hossz")

    perc += int(osszeg/60)
    masodperc += osszeg-(60*perc)
    with open("02_hossz.txt", "w") as f:
        f.write(str(perc) + ":" + str(masodperc))

def leghosszabb_rockzene(zenek = beolvas()):
    leghosszab_index = 0
    leghosszab = 0
    for i in range(0, len(zenek)):
        if zenek[i].get("mufaj") == "rock" and len(zenek[i].get("cim"))>leghosszab:
            leghosszab_index = i
            leghosszab = len(zenek[i].get("cim"))

    with open ("03_leghosszabb_rock.txt", "w") as f:
        f.writelines(zenek[leghosszab_index].get("cim"))

def leggyakoribb_mufaj(zenek = beolvas()):
    mufajok = {}
    feltetel = True
    for i in range(0, len(zenek)):
        for x in range(0, i):
            if zenek[x].get("mufaj") == zenek[i].get("mufaj"):
                feltetel = False

        if feltetel:
            mufajok[zenek[i].get("mufaj")] = 1

        else:
            mufajok[zenek[i].get("mufaj")] += 1

    leggyakoribb = max(mufajok.get())

    with open("04_kedvenc_mufaj.txt", "w") as f:
        f.writelines(mufajok.set(leggyakoribb))


if __name__ == "__main__":
    teljesz_hossz()
    leghosszabb_rockzene()
    leggyakoribb_mufaj()