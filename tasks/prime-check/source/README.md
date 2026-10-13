# Prímszám ellenőrzés

## Feladat

Készíts egy programot, amely bekér egy egész számot, majd kiírja, hogy az prímszám-e. Prímszám az, amely 1-nél nagyobb, és csak 1-gyel és önmagával osztható.

## Követelmények

1. Kérj be egy egész számot, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Hozz létre egy logikai változót, amely azt jelzi, hogy a szám prím-e. Kezdetben akkor legyen igaz, ha a szám nagyobb 1-nél.

   Változó:

   ```py
   prim = változó > 1
   ```

3. Indíts egy ciklust, amely a 2-től a beolvasott számig (azt már nem beleértve) minden számot kipróbál osztónak.

   Ciklus:

   ```py
   for i in range(2, változó):
     # ismétlődő rész
   ```

4. A cikluson belül ellenőrizd, hogy a szám osztható-e `i`-vel. Ha igen, akkor nem prím, ezért állítsd a logikai változót hamisra.

   Feltétel:

   ```py
   if változó % i == 0:
     prim = False
   ```

5. A ciklus után írd ki az eredményt pontosan ezekkel a szövegekkel: `Prímszám` vagy `Nem prímszám`.

   Feltétel és kiírás:

   ```py
   if prim:
     print("szöveg")
   else:
     print("szöveg")
   ```

   Példa: a `7` bemenetre a kimenet `Prímszám`, a `9` bemenetre `Nem prímszám`.

A program az `1`, a `0` és a negatív számok esetén (ezek nem prímek), valamint nagyobb prímszámra (pl. `7919`) is működjön hibátlanul.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a számot (az `input` egyszer meghívódik).
- A kisebb prímszámokat (`2`, `3`, `5`, `7`, `13`) felismeri.
- Az összetett számokra (`4`, `9`, `15`, `100`) azt írja ki, hogy nem prím.
- Az `1` nem prímszám.
- A `0` és a negatív szám (pl. `-7`) nem prímszám.
- A nagy prímszámot (`7919`) is felismeri.

A tesztek a kimenetet pontosan ellenőrzik (`Prímszám` vagy `Nem prímszám`), a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
