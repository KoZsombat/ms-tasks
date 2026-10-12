# Számok ismétlése

## Feladat

Készíts egy programot, amely kiír három számot, megkéri a felhasználót, hogy ismételje meg őket, majd megmondja, egyezik-e a válasz.

## Követelmények

1. Hozz létre egy `nums` nevű listát, amelybe az `"1"`, `"2"`, `"3"` szövegek kerülnek (idézőjelben, mert az `input` is szöveget ad vissza).

   Lista:

   ```py
   változó = ["elem1", "elem2", "elem3"]
   ```

2. Írd ki a számokat szóközzel elválasztva, pl. `repeat this: 1 2 3`.

   Kiírás:

   ```py
   print("szöveg", *lista)
   ```

3. Kérd be a felhasználó válaszát.

   Beolvasás:

   ```py
   változó = input("Kérdés")
   ```

4. Darabold fel a választ a szóközök mentén egy listává.

   Darabolás:

   ```py
   lista = változó.split(" ")
   ```

5. Hasonlítsd össze a két listát. Ha egyeznek, írd ki, hogy `Ügyes vagy`, különben azt, hogy `Nem egyezik meg`.

   Feltétel:

   ```py
   if lista1 == lista2:
     print("szöveg")
   else:
     print("szöveg")
   ```

   Példa:

   ```
   repeat this: 1 2 3
   Válaszod: 1 2 3
   Ügyes vagy
   ```

A program rossz, felcserélt sorrendű és üres válasszal is működjön hiba nélkül.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a választ (az `input` egyszer hívódik meg).
- A program kiírja az `1`, `2`, `3` számokat.
- Helyes válaszra (`1 2 3`) a kimenet tartalmazza az `Ügyes` szót.
- Rossz válaszra (`4 5 6`) a kimenet tartalmazza a `Nem egyezik` szöveget.
- Jó számok rossz sorrendben (`3 2 1`) esetén is a `Nem egyezik` szöveg jelenik meg.
- Üres válaszra is lefut, és a `Nem egyezik` szöveget írja ki.

A kérdés pontos szövegét a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
