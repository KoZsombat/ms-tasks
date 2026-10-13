# Teljes ár

## Feladat

Készíts egy egyszerű programot, amely bekéri három termék árát, majd kiírja a teljes árat.

## Követelmények

1. Kérd be az első termék árát, alakítsd egész számmá, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Ugyanígy kérd be a második és a harmadik termék árát is, külön változókba.

3. Add össze a három árat, és írd ki az eredményt, pl. a `10`, `20` és `30` bemenetre a kiírásban szerepeljen a `60`.

   Kiírás:

   ```py
   print(f"szöveg {változó1 + változó2 + változó3}")
   ```

A program nullás, egyforma és nagy árakkal is működjön hiba nélkül.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program három árat kér be (az `input` háromszor hívódik meg).
- A program kiírja az árak összegét (pl. 10, 20 és 30 esetén 60).
- Más árakkal is helyes az összeg.
- Csupa nulla ár esetén az összeg 0.
- Egyforma árak esetén is helyes az összeg.
- Nagy árak esetén is helyes az összeg.

A kérdések és a kiírás pontos szövegét a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
