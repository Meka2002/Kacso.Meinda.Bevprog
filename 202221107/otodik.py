szavak = []
with open("be.txt", "r", encoding="utf8") as f:
    tartalom = f.readline()
    while tartalom:
        sor = tartalom.split(" ")

        for i in range(0, len(sor)):
            szavak.append(sor[i])
        tartalom = f.readline()

hossz=0
index=0
for x in range(0, len(szavak)):
    if len(szavak[x]) > hossz:
        hossz = len(szavak[x])
        index = x

print(szavak[index])

