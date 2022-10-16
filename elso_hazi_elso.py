def sentence():
    sentence = (input("Adjon meg egy mondatot:"))
    character = []
    Dict = {}
    character.extend(sentence)
    x = 0
    for i in range(0, len(character)):
        x = 0
        for j in range(0, len(character)):
            if character[i] == character[j]:
                x = x + 1
        z = 0
        for k in range(0, i+1):
            if character[k] == character[i]:
                z = z + 1
        if z == 1:
            Dict[character[i]] = x

    print(Dict)
    print(sentence[::-1])
    words = sentence.split(" ")
    print(words)

sentence()