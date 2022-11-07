try:
    file = open("be.txt", "r", encoding="utf8")

    tartalom = file.readlines()

    for sor in tartalom:
        sor = sor.rstrip()
        print(sor)

    file.close()
except FileNotFoundError as fnfe:
    print("A fájl nem található!")