# Faktoriális

## Feladat

Készíts egy egyszerű programot, amely bekér egy pozitív egész számot, majd ciklus segítségével kiszámolja és kiírja a faktoriálisát.

## Követelmények

1. Kérj be egy egész számot, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Hozz létre egy eredmény változót, amelynek a kezdőértéke 1.

   Változó:

   ```py
   eredmény = 1
   ```

3. Indíts egy ciklust, amely az 1, 2, ... a beolvasott számig megy végig. A `range` második száma már nem tartozik bele, ezért a beolvasott számnál eggyel nagyobbat kell megadni.

   Ciklus:

   ```py
   for i in range(1, változó + 1):
     # ismétlődő rész
   ```

4. A cikluson belül szorozd meg az eredményt az aktuális `i` számmal.

   Szorzás:

   ```py
   eredmény = eredmény * i
   ```

5. A ciklus után írd ki az eredményt pontosan ebben a formában: `szám! = eredmény`.

   Kiírás:

   ```py
   print(f"{változó}! = {eredmény}")
   ```

   Példa: az `5` bemenetre a kimenet `5! = 120`.

A program az `1`, a `0` (0! = 1) és nagy szám (pl. `20`) esetén is működjön hibátlanul.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a számot (az `input` egyszer meghívódik).
- Az `5` faktoriálisa (`120`) helyes.
- Az `1` faktoriálisa helyes.
- Egy másik szám (pl. `7`) faktoriálisa is helyes.
- Nagy szám (pl. `20`) faktoriálisa is helyes.
- A `0` faktoriálisa (`1`) is helyes.

A tesztek azt ellenőrzik, hogy az eredmény megjelenik a kimenetben, a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
