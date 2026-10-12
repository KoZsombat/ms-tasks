# Jelszó ellenőrzés

## Feladat

Készíts egy programot, amely bekér egy jelszót, és megmondja, hogy egyezik-e a program által tárolt jelszóval.

## Követelmények

1. Hozz létre egy `password` nevű változót, amelynek értéke a `"password"` szöveg.

   Változó:

   ```py
   változó = "szöveg"
   ```

2. Kérd be a felhasználótól a jelszót, és tárold el egy másik változóban.

   Beolvasás:

   ```py
   változó = input("Kérdés")
   ```

3. Hasonlítsd össze a két szöveget. Ha egyeznek, írd ki, hogy `Helyes`, különben azt, hogy `Nem egyezik meg`.

   Feltétel:

   ```py
   if változó1 == változó2:
     print("szöveg")
   else:
     print("szöveg")
   ```

   Példa:

   ```
   Bemenet: password
   Kimenet: Helyes
   ```

A program kis- és nagybetűre érzékeny (a `Password` nem helyes), és üres vagy ékezetes (pl. `Árvíztűrő`) jelszóval is működjön hiba nélkül.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a jelszót (az `input` egyszer hívódik meg).
- A helyes jelszóra (`password`) a `Helyes` szöveget írja ki.
- Rossz jelszóra a `Nem egyezik` szöveget írja ki.
- A `Password` (nagy kezdőbetűvel) nem fogadható el.
- Üres jelszóra a `Nem egyezik` szöveget írja ki.
- Ékezetes jelszóra is lefut, és a `Nem egyezik` szöveget írja ki.

A kérdés pontos szövegét a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
