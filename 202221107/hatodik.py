sorok = []
toroltsorok = []
with open("sorok.txt", "r") as f:
    sor = f.readline()
    while sor:
        sorok.append(sor)
        sor = f.readline()

for i in range(0, len(sorok)):
    if i != 5-1 and i != 8-1:
        print(sorok[i])
        toroltsorok.append(sorok[i])

with open("sortorles.txt", "w") as f:
    for i in range(0, len(toroltsorok)):
        f.write(toroltsorok[i])