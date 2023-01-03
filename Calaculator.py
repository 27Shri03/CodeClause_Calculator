import math
def calci(a,b,c):
    if c==1:
        print("A+B = ",a+b)
    elif c==2:
        print("A-B = ",a-b)
    elif c==3:
        print("A*B = ",a*b)
    elif c==4:
        if b==0:
            print("Division is not defined , try again")
        else:
            print("A/B = ",a/b)
    elif c==5:
        print("A square",a**2)
        print("B square",b**2)
    elif c==6:
        print("Square root of A: ",math.sqrt(a))
        print("Square root of B: ",math.sqrt(b))
    elif c==7:
        print("A Cube",a**3)
        print("B Cube",b**3)
    elif c==8:
        print("Cube root of A: ",a**(1/3))
        print("Cube root of B: ",b**(1/3))
    elif c==9:
        print("Sin of A: ",math.sin(a))
        print("Sin of B: ",math.sin(b))
    elif c==10:
        g = int(input("Enter base: "))
        print("Log of A: ",math.log(a,g))
        print("Log of B: ",math.log(b,g))
    elif c==11:
        g = int(input("Enter the power: "))
        print("A: ",a**g)
        print("B: ",b**g)        
    else:
        print("Invalid operation")
    
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Square root")
print("7. Cube")
print("8. Cube root")
print("9. Sine")
print("10. Log")
print("11. Power")
print("12. Exit")


while(1):
    a = float(input("Enter First number: "))
    b = float(input("Enter Second number: "))
    c = int(input("Enter the operation: "))
    if c==12:
        print("Exit successfully")
        break
    else:
        calci(a,b,c)
