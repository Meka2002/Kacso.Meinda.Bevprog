class Team:
    def __init__(self, nev, projekt, szerepkor):
        self._nev = nev
        self._projekt = projekt
        self._szerepkor = szerepkor
        print("--Developer létrehozva--")
        print(self._nev, "a", self._projekt, "-en dolgozik", self._szerepkor, "szerepkörben")

    def __eq__(self, masodik):
        return self._projekt == masodik._projekt

host = []
host.append( Team ("Ricsi","SolArch","Frontend"))
host.append( Team ("Angéla","ZerTeng","Tesztelő"))
host.append( Team ("Peti","KefERP","Backend"))
host.append( Team ("Éva","KefERP","Frontend"))

for x in range(0,len(host)-1):
    for z in range(x+1,len(host)):
        if host[x]==host[z]:
            print(host[x]._nev,"és",host[z]._nev,"dolgoznak egy projekten")