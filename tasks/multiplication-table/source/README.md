# Szorzótábla

## Feladat

Készíts egy egyszerű programot, amely bekér egy számot, majd kiírja a szorzótábláját 1-től 10-ig.

## Követelmények

1. Kérj be egy egész számot, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Indíts egy ciklust, amely az 1, 2, ... 10 számokon megy végig. A `range` második száma már nem tartozik bele, ezért 11-et kell megadni.

   Ciklus:

   ```py
   for i in range(1, 11):
     # ismétlődő rész
   ```

3. A cikluson belül minden körben írj ki egy sort pontosan ebben a formában: `szám * i = eredmény`.

   Kiírás:

   ```py
   print(f"{változó} * {i} = {változó * i}")
   ```

   Példa: az `5` bemenetre az első sor `5 * 1 = 5`, az utolsó `5 * 10 = 50`.

A program nullával, negatív számmal (pl. `-3`) és nagy számmal (pl. `123456`) is működjön hibátlanul.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a számot (az `input` egyszer meghívódik).
- A program pontosan tíz sort ír ki.
- Az `5` szorzótáblája helyes, a megadott formában.
- Egy másik szám (pl. `7`) szorzótáblája is helyes.
- A `0` szorzótáblája is helyes.
- Negatív és nagy szám szorzótáblája is helyes.

A tesztek a kiírt sorok pontos formáját ellenőrzik (`5 * 3 = 15`), a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
