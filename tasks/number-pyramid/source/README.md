# Számpiramis

## Feladat

Készíts egy programot, amely bekér egy sorszámot, majd annyi sort ír ki, hogy minden sor eggyel több számot tartalmaz az előzőnél: az első sorban `1`, a másodikban `1 2`, a harmadikban `1 2 3`, és így tovább.

## Követelmények

1. Kérj be egy egész számot (a sorok számát), és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Indíts egy külső ciklust, amely az 1, 2, ... a sorok számáig megy végig (a `range` második száma már nem tartozik bele, ezért eggyel nagyobbat adj meg). Ez a ciklus adja a sorokat.

   Ciklus:

   ```py
   for i in range(1, változó + 1):
     # ismétlődő rész
   ```

3. A külső cikluson belül hozz létre egy üres szöveget a sor számára.

   Szöveg:

   ```py
   sor = ""
   ```

4. Indíts egy belső ciklust, amely 1-től az aktuális `i` számig megy. Minden körben fűzd hozzá a számot és egy szóközt a sorhoz.

   Ciklus és hozzáfűzés:

   ```py
   for j in range(1, i + 1):
     sor = sor + str(j) + " "
   ```

5. A belső ciklus után írd ki a sort. A végén maradó szóközt a `strip()` törli.

   Kiírás:

   ```py
   print(sor.strip())
   ```

   Példa: a `3` bemenetre a kimenet:

   ```
   1
   1 2
   1 2 3
   ```

A program az `1`, a `0` (ilyenkor nem ír ki semmit) és kétjegyű számokat is tartalmazó piramis (pl. `12` sor) esetén is működjön hibátlanul.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a sorok számát (az `input` egyszer meghívódik).
- A program pontosan annyi sort ír ki, amennyit kértek.
- Az `5` soros piramis helyes, a megadott formában.
- Az `1` soros piramis helyes.
- A `12` soros piramis (kétjegyű számokkal) is helyes.
- A `0` bemenetre nem íródik ki semmi.

A tesztek a sorok pontos formáját ellenőrzik (`1 2 3`), a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
