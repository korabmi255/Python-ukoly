zakladni_cena=500
#vstup
vek= float(input("Zadejte věk: "))
je_student= input("Jste student? (ano/ne): ")
pocet_osob= int(input("Zadejte počet osob: "))

#urceni slevy

if pocet_osob>= 4:
    typ_slevy="SKupinova sleva"
    cena= zakladni_cena - 0.25* zakladni_cena

elif je_student=="ano" and vek < 26:
    typ_slevy="Studentska sleva"
    cena= zakladni_cena - 0.30* zakladni_cena

elif vek >= 65:
    typ_slevy="Seniorska sleva"
    cena= zakladni_cena - 0.20* zakladni_cena

    #celkova cena
celkem= cena * pocet_osob

#vystup
print("Typ slevy:", typ_slevy)
print("Cena za 1 listek:", cena, "Kč")
print("Celková cena:", celkem, "Kč")





