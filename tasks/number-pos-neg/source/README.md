# Pozitív, negatív vagy nulla

## Feladat

Készíts egy egyszerű programot, amely bekér egy egész számot, majd kiírja, hogy a szám pozitív, negatív vagy nulla.

## Követelmények

1. Kérj be egy egész számot, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Vizsgáld meg a számot feltételekkel: először azt, hogy nulla-e, utána azt, hogy kisebb-e nullánál, minden más esetben a szám pozitív.

   Feltétel:

   ```py
   if változó == 0:
     # teendő
   elif változó < 0:
     # teendő
   else:
     # teendő
   ```

3. Mindhárom esetben írd ki a megfelelő mondatot pontosan így:

   - nulla esetén: `A szám nulla`
   - negatív szám esetén: `A szám negatív`
   - pozitív szám esetén: `A szám pozitív`

   Kiírás:

   ```py
   print("szöveg")
   ```

   Példa: a `5` bemenetre a kiírás `A szám pozitív`.

A program a nullához közeli számokkal (`1`, `-1`) és nagyon nagy számokkal (pl. `1000000000`) is működjön hibátlanul.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a számot (az `input` egyszer meghívódik).
- A pozitív számot felismeri, és csak a pozitív mondatot írja ki.
- A negatív számot felismeri, és csak a negatív mondatot írja ki.
- A nullát felismeri, és csak a nulla mondatot írja ki.
- A nullához közeli számokat (`1` és `-1`) helyesen osztályozza.
- A nagyon nagy pozitív és negatív számokat is helyesen osztályozza.

A tesztek a három kiírt mondat pontos szövegét ellenőrzik, a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
