# Výpočet celkové výmeny bytu v m2

def obsah_obdelnika(a,b) :          #funkce pro výpočet výměry pokoje
    if a <= 0 or b <= 0:
        return None
    obsah = a * b
    return obsah                    #return a * b

print ("Program pro celkovou výměru bytu")
pocet_pokoju = int(input("Zadej počet pokojů: "))

pokoj=1                             # začíname prvním pokojem
celkova_vymena = 0
while pokoj <= pocet_pokoju:
    print (f"Zadej rozměry {pokoj}. mistnosti")
    strana_a = float(input("Zadej stranu a: "))
    strana_b = float(input("Zadej stranu b: "))
    rozloha_pokoje = obsah_obdelnika(strana_a, strana_b)
    if rozloha_pokoje != None:
        celkova_vymena += rozloha_pokoje
        pokoj += 1
    else:
        print("chbné zadání, opakuji!")

if (pocet_pokoju > 0):
    print(f"Celková výměra bytu je: {celkova_vymena} m2")
else:
    print("Zadej kladný počet místnosti")


print(f"Celková výměra bytu je: {celkova_vymena} m2")