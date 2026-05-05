# ÚLOHA 1: Zvětšovač (použij +=)
cislo = int(input("Zadej číslo: "))
# Sem doplň kód:
# 1. Zvětšovač
cislo = float(input("Zadej číslo: "))
cislo += 10
print(f"Výsledek: {cislo}")

# 2. Útrata v hospodě
ucet = float(input("Zadej celkovou sumu účtu: "))
lidi = int(input("Zadej počet lidí: "))
castka_na_osobu = ucet / lidi
print(f"Každý zaplatí: {round(castka_na_osobu, 2)} Kč")

# 3. Plocha kruhu
r = float(input("Zadej poloměr kruhu (r): "))
S = 3.14 * (r ** 2)
print(f"Plocha kruhu je: {round(S)}")

# ÚLOHA 2: Útrata (zaokrouhli na 2 místa)
celkem = float(input("Celková suma (Kč): "))
lidi = int(input("Počet lidí: "))
# Sem doplň výpočet a print s round():
# Načteme celkovou útratu (může to být číslo s haléři, proto float)
ucet = float(input("Zadej celkovou sumu účtu: "))

# Počet lidí musí být celé číslo, proto použijeme int()
lidi = int(input("Zadej počet lidí: "))

# Vypočítáme částku na jednu osobu klasickým dělením
castka_na_osobu = ucet / lidi

# Funkce round() zde bere dva argumenty: samotné číslo a počet desetinných míst (2)
# Výsledek vložíme rovnou do f-stringu k vypsání.
print(f"Každý zaplatí: {round(castka_na_osobu, 2)} Kč")
# Načteme poloměr, což opět může být desetinné číslo
r = float(input("Zadej poloměr kruhu (r): "))

# Vzorec pro obsah je S = π * r². 
# Dvě hvězdičky (**) v Pythonu znamenají umocňování, tedy r ** 2 je poloměr na druhou.
S = 3.14 * (r ** 2)

# Pokud funkci round() zadáme jen jeden argument (číslo), automaticky ho zaokrouhlí na nejbližší celé číslo.
print(f"Plocha kruhu je: {round(S)}")

# ÚLOHA 3: Plocha kruhu (zaokrouhli na celé číslo)
r = float(input("Zadej poloměr: "))
# plocha = 3.14 * r * r
# Sem doplň kód:
