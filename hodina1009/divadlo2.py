
zakladni_cena = 500

# 1.pocet osob
pocet_osob = int(input("Zadejte počet osob: "))

# 2. kdyz jich bude vic jak 4 dame cenu
if pocet_osob >= 4:
    typ_slevy = "Skupinová sleva"
    cena = zakladni_cena - (zakladni_cena * 0.25)

# 3. kdyz jich bude min jak 4 zeptame se na vek
else:
    vek = int(input("Zadejte věk: "))
    
    if vek >= 65:
        typ_slevy = "Seniorská sleva"
        cena = zakladni_cena - (zakladni_cena * 0.20)
    elif vek < 26:
        je_student = input("Jste student? (ano/ne): ")
        if je_student == "ano":
            typ_slevy = "Studentská sleva"
            cena = zakladni_cena - (zakladni_cena * 0.30)
        else:
            typ_slevy = "Bez slevy"
            cena = zakladni_cena
    else:
        typ_slevy = "Bez slevy"
        cena = zakladni_cena

# Celková cena za všechny osoby
celkem = cena * pocet_osob

# Výsledek
print("Typ slevy:", typ_slevy)
print("Cena za 1 lístek:", cena, "Kč")
print("Celková cena:", celkem, "Kč")
