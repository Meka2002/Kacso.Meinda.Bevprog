z=5

def hanyados():
    a = int(input("Enter 'a' value:"))
    b = int(input("Enter 'b' value:"))
    print(a /b)
while z==5:
    try:
       hanyados()


    except ZeroDivisionError:
        print("Division by zero not allowed")

    finally:
        print("Out of try except blocks")