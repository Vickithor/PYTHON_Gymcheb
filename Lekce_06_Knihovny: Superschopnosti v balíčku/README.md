# Lekce 6: Knihovny – Superschopnosti v balíčku

V předchozích lekcích jste se naučili, jak program větvit pomocí podmínek. Dnes tyto dovednosti posuneme na novou úroveň. Naučíme se do našeho kódu přivolat "pomocníky" – tzv. **knihovny**, které nám umožní ovládnout náhodu nebo zastavit čas.

### Co jsou to knihovny?

Představte si Python jako základní sadu **LEGO**. Máte v ní kostičky, které do sebe zapadají, ale občas by se vám hodil speciální dílek – třeba motor, světýlko nebo dálkové ovládání. 

Knihovna je přesně taková krabička se speciálními dílky, kterou si k projektu "připojíte". V Pythonu k tomu používáme magické slůvko:

`python`

`import nazev_knihovny`

### Knihovna random: Pán chaosu

Tato knihovna umožňuje programu generovat náhodná čísla. To je naprostý základ pro hry (hod kostkou), simulace nebo šifrování.
1. Celá čísla: **random.randint(a, b)**

    Co dělá: Vybere náhodné celé číslo.

    Pozor na hranice: V Pythonu jsou u této funkce obě hranice zahrnuty.

    Příklad: `random.randint(1, 3)` může hodit 1, 2, nebo 3.

2. Desetinná čísla: **random.uniform(a, b)**

    Co dělá: Pokud potřebujete náhodnou cenu, váhu nebo polohu, sáhněte po uniform. Vygeneruje náhodné desetinné číslo (float).

    Příklad: `vaha = random.uniform(1.0, 5.0)` hodí třeba 3.4215...

3. Šance a pravděpodobnost: **random.random()**

    Co dělá: Hodí náhodné číslo v rozmezí 0.0 až 1.0.

    Využití: Často se používá k výpočtu šance. Například 0.7 znamená 70% šanci na úspěch.

### Knihovna time: Vládce časové osy

Knihovna time neslouží jen k "uspání" programu, ale i k měření toho, jak dlouho vaše výpočty trvají.
1. **time.sleep(sekundy)**

Zastaví vykonávání programu na zadanou dobu. Nemusíte čekat jen celé sekundy!

`time.sleep(0.5)` – pauza na půl sekundy.

`time.sleep(0.1)` – vytvoří efekt rychlého blikání.

2. **time.time()** – Čas v sekundách

Tato funkce vrací obrovské číslo (počet sekund od roku 1970). Skvěle se hodí pro tvorbu stopek.

### Záchranná brzda: Co když se to rozbije?

**Pozor na nekonečné spaní!**
Pokud omylem napíšete `time.sleep(3600)`, váš program bude celou hodinu "mrtvý" a nebude reagovat.

Pokud se vám to stane (nebo se program zacyklí), nezmatkujte. Stačí v terminálu stisknout:
**Ctrl + C**

Tato zkratka program okamžitě a násilně ukončí.
