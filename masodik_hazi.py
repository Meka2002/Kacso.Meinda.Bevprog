def triangle():
    print("Adja meg a háromszög három oldalát cm-ben")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))
    if a+b>=c and a+c>=b and b+c>=a:
        print("A",a,",",b ,"és",c,"oldalú háromszög megszerkeszthető")
    else:
        print("A",a,",",b,"és",c,"oldalú háromszög NEM szerkezdhető")

triangle()