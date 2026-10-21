a=float (input("Zadej první číslo: "))
b=float (input("Zadej druhé číslo: "))
c=float (input("Zadej třetí číslo: "))
min = a
max = a
if b < min:
    min = b
else:
    if b > max:
        max = b
if c < min:
    min = c
else:
    if c > max:
        max = c
print (f"Minimum: {min}\nMaximum: {max}")

