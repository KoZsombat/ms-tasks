# Alapműveletek

## Feladat

Készíts egy programot, amely négy függvényt tartalmaz (összeadás, kivonás, szorzás, osztás), majd kiírja mindegyik eredményét az `1` és `2` számokra.

## Követelmények

1. Írj egy `add(a, b)` függvényt, amely visszaadja a két szám összegét.

   Függvény:

   ```py
   def függvény(a, b):
     return a + b
   ```

2. Írj egy `subtract(a, b)` függvényt, amely visszaadja `a - b` értékét.

3. Írj egy `multiply(a, b)` függvényt, amely visszaadja a két szám szorzatát.

4. Írj egy `divide(a, b)` függvényt, amely visszaadja `a / b` értékét. Ha `b` értéke `0`, akkor `0`-t adjon vissza (nullával nem lehet osztani).

   Feltétel:

   ```py
   if feltétel:
     return érték
   else:
     return másikÉrték
   ```

5. Hívd meg mind a négy függvényt az `1` és `2` számokkal, és írd ki az eredményeket egy-egy sorba.

   Függvényhívás és kiírás:

   ```py
   print(f"szöveg {függvény(1, 2)}")
   ```

   Példa kimenet:

   ```
   Add 3
   Subtract -1
   Multiply 2
   Divide 0.5
   ```

A `divide` függvény nullával osztásnál is működjön hiba nélkül, és a függvények negatív számokkal is helyesen számoljanak.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- Az `add` függvény helyesen adja össze a két számot.
- A `subtract` függvény helyesen vonja ki a második számot az elsőből.
- A `multiply` függvény helyesen szorozza össze a két számot.
- A `divide` függvény helyesen osztja el a két számot.
- A `divide` függvény nullával osztáskor `0`-t ad vissza.
- A program négy sort ír ki, benne a négy eredménnyel (`3`, `-1`, `2`, `0.5`).

A kiírt szövegek pontos szövegét (pl. `Add`) a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
