# Dolgozatpontok

## Feladat

Készíts egy programot, amely egy osztály dolgozatpontszámaiból kiszámolja az átlagot, a legmagasabb pontszámot és azt, hogy hány tanuló ment át.

## Követelmények

1. Hozz létre egy `scores` nevű listát ezekkel a pontszámokkal: `20, 40, 60, 80, 85`.

   Lista:

   ```py
   változó = [1, 2, 3]
   ```

2. Írj egy `passed` nevű függvényt, amely egy pontszámot kap paraméterként, és `True`-t ad vissza, ha a pontszám legalább `40`, különben `False`-t.

   Függvény:

   ```py
   def függvény(paraméter):
     return paraméter >= szám
   ```

3. Számold ki a pontszámok átlagát: add össze őket a `sum` függvénnyel, és oszd el a darabszámukkal (`len`).

   Összeg és darabszám:

   ```py
   sum(lista) / len(lista)
   ```

4. Keresd meg a legmagasabb pontszámot a `max` függvénnyel.

   Legnagyobb elem:

   ```py
   max(lista)
   ```

5. Számold meg, hány tanuló ment át: válogasd ki a `passed` függvénnyel az átment pontszámokat a `filter` segítségével, és számold meg őket.

   Szűrés és számolás:

   ```py
   len(list(filter(függvény, lista)))
   ```

6. Írd ki egy sorban a három eredményt, pl. `Átlag: 57.0, legmagasabb: 85, átment 4 tanuló`.

   Kiírás:

   ```py
   print(f"szöveg {érték1}, szöveg {érték2}")
   ```

A program semmit ne kérjen be a felhasználótól, és a pontosan `40` pontos tanuló is átmentnek számítson.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program kiírja az átlagot (`57.0`).
- A program kiírja a legmagasabb pontszámot (`85`).
- A program kiírja az átment tanulók számát (`4`).
- A `passed` függvény `True`-t ad vissza 40 és annál több pontra.
- A `passed` függvény `False`-t ad vissza 40-nél kevesebb pontra.
- A program nem kér be adatot (`input` nem hívódik meg).

A kiírt szöveg pontos megfogalmazását a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
