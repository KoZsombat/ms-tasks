# Pontszám és jegy

## Feladat

Készíts egy egyszerű programot, amely bekéri az elért pontszámot, majd kiírja a hozzá tartozó jegyet (1-től 5-ig).

## Követelmények

1. Kérd be az elért pontszámot, alakítsd egész számmá, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Döntsd el feltételekkel, hogy melyik jegy jár a pontszámra:

   - 40 pont alatt: `1`
   - 40 ponttól 60 pont alatt: `2`
   - 60 ponttól 80 pont alatt: `3`
   - 80 ponttól 90 pont alatt: `4`
   - 90 ponttól: `5`

   Feltétel:

   ```py
   if változó < szám:
     # teendő
   elif változó < másik_szám:
     # teendő
   else:
     # teendő
   ```

3. Írd ki a jegyet egyedül, más szöveg nélkül, pl. a `75` bemenetre a kiírás `3`.

   Kiírás:

   ```py
   print("szöveg")
   ```

A program a határértékekkel (pl. `39`, `40`, `59`, `60`, `79`, `80`, `89`, `90`), a `0` és a `100` ponttal is működjön hibátlanul.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a pontszámot (az `input` egyszer meghívódik).
- 40 pont alatt (pl. `0`, `20`, `39`) a jegy `1`.
- 40 és 59 pont között a jegy `2`.
- 60 és 79 pont között a jegy `3`.
- 80 és 89 pont között a jegy `4`.
- 90 ponttól (pl. `90`, `95`, `100`) a jegy `5`.

A tesztek azt ellenőrzik, hogy a kimenet pontosan a jegy, más szöveg nélkül; a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
