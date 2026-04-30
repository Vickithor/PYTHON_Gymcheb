# Micro:bit & Python (v editoru Mu)

Pro seznámení s textovým programováním v jazyce MicroPython budeme používat přátelské a intuitivní prostředí [Mu Editor](https://codewith.mu/). 

Do začátků i pro pokročilejší experimentování vám bude skvělým pomocníkem tento oficiální výukový průvodce pro [Micro:bit](https://codewith.mu/en/tutorials/1.2/microbit), kde najdete spoustu praktických ukázek a vysvětlení.


## Syntaxe
### 1. Start programu
Každý program musí začínat tímto řádkem, aby Micro:bit věděl, co má dělat:
`from microbit import *`


### 2. Displej (Oči Micro:bitu)
```# Zobrazení přednastaveného obrázku (např. srdce, úsměv, křížek)
display.show(Image.HEART)
display.show(Image.NO)     # Křížek
display.show(Image.YES)    # Fajfka

# Běžící text (scrolling)
display.scroll("AHOJ")

# Vymazání displeje (zhasnutí všech diod)
display.clear()
```


### 3. Tlačítka (Vstupy od uživatele)
```# Zjištění, zda je tlačítko A právě teď stisknuté
if button_a.is_pressed():
    # udělej něco

# Zjištění, zda bylo tlačítko B stisknuto (a uvolněno) od poslední kontroly
if button_b.was_pressed():
    # udělej něco
```

### 4. Akcelerometr (Pohyb a třesení)
```


### 5. Teploměr (Měření prostředí)


### 6. Zvuk (Pípání a melodie)
**Pozor:** Pro zvuk je nutné na úplný začátek programu přidat import music.

<br>
---------------------------------------------------------------------------------------------------------------------------------

**Největší šok** při přechodu z MakeCode do Pythonu je to, že kód proběhne jen jednou a skončí.

Aby Micro:bit neustále kontroloval tlačítka (jako blok Vždy ve Scratchi/MakeCode), musí být vše **zabaleno v nekonečném cyklu**.
```
from microbit import *

# Zde se píše kód, který se provede jen jednou po startu (např. úvodní smajlík)

while True:
    # Zde se píše kód, který běží neustále dokola (kontrola tlačítek, teploty...)
    ```
