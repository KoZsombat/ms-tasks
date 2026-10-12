# Történet ágak

## Feladat

Készíts egy programot, amely megkérdezi a felhasználótól, melyik történetszálat választja (`1` vagy `2`), majd kiírja, melyiket választotta.

## Követelmények

1. Kérd be a választást a felhasználótól, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = input("Kérdés")
   ```

2. Ha a választás `1`, írd ki, hogy az első vonalat választotta. Figyelj rá, hogy az `input` mindig szöveget ad vissza, ezért a `"1"` szöveggel (idézőjelben) hasonlítsd össze.

   Feltétel:

   ```py
   if változó == "érték":
     print("szöveg")
   ```

3. Ha a választás `2`, írd ki, hogy a második vonalat választotta.

   További feltétel:

   ```py
   elif változó == "érték":
     print("szöveg")
   ```

4. Minden más esetben írd ki, hogy rossz a bemenet.

   Különben ág:

   ```py
   else:
     print("szöveg")
   ```

   Példa:

   ```
   Bemenet: 1
   Kimenet: első vonalat választottad
   ```

A program üres bemenettel és érvénytelen értékkel (pl. `3`) is működjön hiba nélkül.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a választást (az `input` egyszer hívódik meg).
- Az `1` választásra a kimenet tartalmazza az `első` szót.
- A `2` választásra a kimenet tartalmazza a `második` szót.
- Érvénytelen értékre (pl. `3`) a kimenet tartalmazza a `rossz` szót.
- Üres bemenetre a kimenet tartalmazza a `rossz` szót.
- A három eset (`1`, `2`, érvénytelen) különböző kimenetet ad.

A kérdés szövegét a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
