# Egyszerű kamat

## Feladat

Készíts egy egyszerű programot, amely bekéri a tőkét, az éves kamatlábat és az időt, majd kiírja az egyszerű kamat összegét.

## Követelmények

1. Kérd be a tőkét, alakítsd egész számmá, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Kérd be az éves kamatlábat százalékban (pl. `5` az 5%-ot jelenti), szintén egész számként, egy másik változóba.

3. Kérd be az időt években, egész számként, egy harmadik változóba.

4. Számold ki a kamatot: szorozd össze a tőkét, a kamatlábat és az időt, majd told el 100-zal. Írd ki az eredményt, pl. `1000` tőke, `5` kamatláb és `3` év esetén a kiírásban szerepeljen a `150.0`.

   Kiírás:

   ```py
   print(f"szöveg {változó1 * változó2 * változó3 / 100}")
   ```

A program tizedes eredménnyel (pl. `150` tőke, `5` kamatláb és `1` év esetén `7.5`), nulla évvel, nulla százalékos kamatlábbal és nagy számokkal is működjön hiba nélkül.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program három értéket kér be (az `input` háromszor hívódik meg).
- A program kiírja a kamatot (pl. 1000 tőke, 5% és 3 év esetén 150).
- Tizedes eredmény esetén is helyes a kamat (pl. 150 tőke, 5% és 1 év esetén 7.5).
- Nulla év esetén a kamat 0.
- Nulla százalékos kamatláb esetén a kamat 0.
- Nagy számoknál is helyes a kamat.

A kérdések és a kiírás pontos szövegét a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
