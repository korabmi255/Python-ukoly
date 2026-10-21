a=float (input("Zadej 1 číslo: "))
b=float (input("Zadej 2 číslo: "))
c=float (input("Zadej 3 číslo: "))

#např. 7,10,2
if a > b:
    p = a
    a = b
    b = p 
    # (1): 7.10.9
if b > c:
    p = b
    b = c
    c = p
    #(2): 7,2,10
if a > b:
    p = b
    a = b
    b = p
    #(3): 2,7,10

print(f"{a}<{b}<{c}")