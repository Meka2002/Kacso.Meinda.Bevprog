def cm_inc():
    print("Adjon meg egy számot és egy mértékegységet (cm/inch)")
    numbers = float(input())
    cm_inch = input()
    if cm_inch == "cm":
        print(numbers/2.54, " inches")
    elif cm_inch == "inch":
        print(numbers*2.54, " cmes")
    else:
        print("Not correct unit!")

cm_inc()