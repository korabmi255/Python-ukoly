# vyhodnoceni kolize
 
# kolizeni  doména (obdelník)
x1 = 2
y1 = 1.5
x2 = 6
y2 = 7

# bod (panáček
xb = float(input("Zadej x souřadnici panáčka: "))
yb = float(input("Zadej y souřadnici panáčka: "))

#test kolize
if xb>=x1 and xb<=x2 and yb>=y1 and yb<=y2:
    print("kolize bodu s obdelníkem")
else:
    print("bez kolize")

if xb<x1 or xb>x2 or yb<y1 or yb>y2:
    print("bez kolize")
else:
    print("kolize bodu s obdelníkem")

