# A. Plny ctverec
def ctverec(delka):
    if delka <= 0: return None
    radek = 0
    while radek < delka:
        print("*" * delka)
        radek = radek + 1

# B. Plny obdelnik
def obdelnik(sirka, vyska):
    if sirka <= 0 or vyska <= 0: return None
    radek = 0
    while radek < vyska:
        print("*" * sirka)
        radek = radek + 1

# C. Prazdny ctverec
def prazdny_ctverec(delka):
    if delka <= 0: return None
    radek = 0
    while radek < delka:
        if radek == 0 or radek == delka - 1:
            print("*" * delka)
        else:
            print("*" + " " * (delka - 2) + "*")
        radek = radek + 1

# D. Prazdny obdelnik
def prazdny_obdelnik(sirka, vyska):
    if sirka <= 0 or vyska <= 0: return None
    radek = 0
    while radek < vyska:
        if radek == 0 or radek == vyska - 1:
            print("*" * sirka)
        else:
            print("*" + " " * (sirka - 2) + "*")
        radek = radek + 1

# E. Levy trojuhelnik
def levy_trojuhelnik(delka):
    if delka <= 0: return None
    radek = 1
    while radek <= delka:
        print("*" * radek)
        radek = radek + 1

# F. Pravy trojuhelnik
def pravy_trojuhelnik(delka):
    if delka <= 0: return None
    radek = 1
    while radek <= delka:
        print(" " * (delka - radek) + "*" * radek)
        radek = radek + 1

# G. Rovnoramenny trojuhelnik
def rovnoramenny_trojuhelnik(delka):
    if delka <= 0: return None
    if delka % 2 == 1: hvezdy = 1
    else: hvezdy = 2
    while hvezdy <= delka:
        print(" " * ((delka - hvezdy) // 2) + "*" * hvezdy)
        hvezdy = hvezdy + 2

# --- HLAVNI PROGRAM ---
print("VITEJ V PROGRAMU PRO KRESLENI GEOMETRICKYCH TVARU")
znovu = "ano"

while znovu == "ano":
    tvar = input("Jaky obrazec chces vykreslit? ")
    delka = int(input("Zadej velikost (sirku/zakladnu): "))
    
    if tvar == "c": ctverec(delka)
    elif tvar == "cn": prazdny_ctverec(delka)
    elif tvar == "o": obdelnik(delka, int(input("Zadej vysku: ")))
    elif tvar == "on": prazdny_obdelnik(delka, int(input("Zadej vysku: ")))
    elif tvar == "tpl": levy_trojuhelnik(delka)
    elif tvar == "tpp": pravy_trojuhelnik(delka)
    elif tvar == "tr": rovnoramenny_trojuhelnik(delka)
    else: print("Neznamy tvar")
        
    znovu = input("Chces vykreslit dalsi obrazec? ")

print("DEKUJI ZA POUZITI PROGRAMU")