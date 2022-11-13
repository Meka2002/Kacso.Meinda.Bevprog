import string
mondatok = []

def Tisztitas(sor):
    sor = sor
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    irasjel_nelkul = ""
    maganhangzo_nelkul = ""
    szokoz_nelkul = ""
    for x in sor:
        if x not in string.punctuation:
            irasjel_nelkul += x

    for i in irasjel_nelkul:
        if i not in maganhangzok:
            maganhangzo_nelkul += i

    for z in maganhangzo_nelkul:
        if z != " ":
            szokoz_nelkul += z

    return szokoz_nelkul

def file_be(filename):

    with open(filename, 'r', encoding='utf8') as f:
        tartalom = f.readline()
        while tartalom:
            tisztitott = Tisztitas(tartalom)
            mondatok.append(tisztitott)
            tartalom = f.readline()


if __name__ == "__main__":
    file_be("hazi.txt")
    ures_nelkul = []
    for x in range(0, len(mondatok)):
        if len(mondatok[x]) != 1:
            ures_nelkul.append(mondatok[x])

    with open("ki.txt", "w") as f:
        f.writelines(ures_nelkul)

