# Átlagsebesség

## Feladat

Készíts egy egyszerű programot, amely bekéri a megtett távolságot és az utazás idejét, majd kiírja az átlagsebességet km/h-ban.

## Követelmények

1. Kérd be a megtett távolságot kilométerben, alakítsd egész számmá, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Kérd be az utazás idejét órában, szintén egész számként, egy másik változóba.

3. Számold ki az átlagsebességet: oszd el a távolságot az idővel, és írd ki az eredményt, pl. `120` km és `2` óra esetén a kiírásban szerepeljen a `60.0`.

   Kiírás:

   ```py
   print(f"szöveg {változó1 / változó2}")
   ```

A program tizedes eredménnyel (pl. `100` km és `8` óra esetén `12.5`), nulla távolsággal és nagy számokkal is működjön hiba nélkül. Nulla órával nem kell foglalkoznod.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program két értéket kér be (az `input` kétszer hívódik meg).
- A program kiírja az átlagsebességet (pl. 120 km és 2 óra esetén 60).
- Tizedes eredmény esetén is helyes a sebesség (pl. 100 km és 8 óra esetén 12.5).
- Egy órás utazásnál a sebesség megegyezik a távolsággal.
- Nulla távolság esetén a sebesség 0.
- Nagy számoknál is helyes a sebesség.

A kérdések és a kiírás pontos szövegét a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
