# Téglalap területe

## Feladat

Készíts egy egyszerű programot, amely bekéri egy téglalap két oldalának hosszát, majd kiírja a területét.

## Követelmények

1. Kérd be az első oldal hosszát, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = input("Kérdés")
   ```

2. Kérd be a második oldal hosszát is, és tárold el egy másik változóban.

   Beolvasás:

   ```py
   másik_változó = input("Kérdés")
   ```

3. Az `input` szöveget ad vissza, ezért alakítsd mindkét értéket egész számmá, és szorozd össze őket.

   Átalakítás és szorzás:

   ```py
   int(változó) * int(másik_változó)
   ```

4. Írd ki a kapott területet, pl. a `3` és `4` bemenetre a kiírásban szerepeljen a `12`.

   Kiírás:

   ```py
   print(f"szöveg {kifejezés}")
   ```

A program egyenlő oldalakkal (négyzet), nullával és nagy számokkal is működjön hiba nélkül.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program két értéket kér be (az `input` kétszer hívódik meg).
- A program kiírja a területet (pl. 3 és 4 esetén 12).
- Más számokkal is helyes a terület.
- Egyenlő oldalak esetén is helyes a terület.
- Nulla hosszúságú oldal esetén a terület 0.
- Nagy számoknál is helyes a terület.

A kérdések és a kiírás pontos szövegét a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
