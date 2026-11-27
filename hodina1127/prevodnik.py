# převod zbytku na znak (0-9 a A-F)
def cifra_na_znak(hodnota):
    if hodnota < 10:
        return str(hodnota)
    if hodnota == 10:
        return "A"
    if hodnota == 11:
        return "B"
    if hodnota == 12:
        return "C"
    if hodnota == 13:
        return "D"
    if hodnota == 14:
        return "E"
    if hodnota == 15:
        return "F"

# převod DEC do jiné číselné soustavy
def preved_soustavu(cislo, zaklad):
    if cislo < 0:
        return None
    if zaklad != 2 and zaklad != 8 and zaklad != 10 and zaklad != 16:
        return None
    if cislo == 0:
        return "0"

    prevedene_cislo = ""
    while cislo > 0:
        zbytek = cislo % zaklad
        cislo //= zaklad
        prevedene_cislo = cifra_na_znak(zbytek) + prevedene_cislo
    return prevedene_cislo

# --- 1. ZADÁNÍ VLASTNÍHO ČÍSLA ---
moje_cislo = int(input("Zadej nezáporné číslo v desítkové soustavě: "))
print("Dvojkově (BIN):", preved_soustavu(moje_cislo, 2))
print("Osmičkově (OCT):", preved_soustavu(moje_cislo, 8))
print("Šestnáctkově (HEX):", preved_soustavu(moje_cislo, 16))
print()

# --- 2. POVINNÁ PŘEVODNÍ TABULKA ---
print("DEC | BIN   | OCT | HEX")
print("-------------------------")

cislo = 0
while cislo <= 16:
    print(cislo, "|", preved_soustavu(cislo, 2), "|", preved_soustavu(cislo, 8), "|", preved_soustavu(cislo, 16))
    cislo += 1

# kontrola chyb
print("Test neplatného čísla:", preved_soustavu(-5, 2))
print("Test neplatného základu:", preved_soustavu(10, 5))
    