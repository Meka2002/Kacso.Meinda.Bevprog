def kiolvas(sorszam):
    with open("be.txt", "r", encoding="utf8") as f:
        for i in range(0, sorszam):
            sor = f.readline()
            print(sor)


if __name__ == "__main__":
    kiolvas(int(input("Kérem adja meg a kiirandó sorok számát:")))