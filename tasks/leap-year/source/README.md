# Szökőév

## Feladat

Készíts egy egyszerű programot, amely bekér egy évszámot, majd kiírja, hogy az adott év szökőév-e.

## Követelmények

1. Kérj be egy évszámot, alakítsd egész számmá, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Döntsd el, hogy szökőév-e. Egy év szökőév, ha

   - osztható 400-zal, **vagy**
   - osztható 4-gyel, **de nem** osztható 100-zal.

   A maradékot a `%` jellel kapod meg, a feltételeket az `and` (és) és az `or` (vagy) köti össze.

   Feltétel:

   ```py
   if (változó % szám == 0) or (változó % szám == 0 and változó % szám != 0):
     # teendő
   else:
     # teendő
   ```

3. Írd ki a megfelelő mondatot pontosan így:

   - szökőév esetén: `Szökő év`
   - ha nem szökőév: `Nincs szökő év`

   Kiírás:

   ```py
   print("szöveg")
   ```

   Példa: a `2024` bemenetre a kiírás `Szökő év`, az `1900` bemenetre `Nincs szökő év`.

A program a századfordulós évekkel is működjön helyesen (pl. `1900` és `2100` nem szökőév, `2000` és `1600` az).

## Értékelés

A megoldást 5 teszt ellenőrzi (1-1 pont):

- A program bekéri az évszámot (az `input` egyszer meghívódik).
- A néggyel osztható éveket (pl. `2024`) szökőévnek jelzi.
- A néggyel nem osztható éveket (pl. `2023`) nem szökőévnek jelzi.
- A 100-zal osztható, de 400-zal nem osztható éveket (pl. `1900`, `2100`) nem szökőévnek jelzi.
- A 400-zal osztható éveket (pl. `2000`) szökőévnek jelzi.

A tesztek a két kiírt mondat pontos szövegét ellenőrzik, a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
