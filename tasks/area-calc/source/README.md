# Területszámítás

## Feladat

Írj két függvényt: az egyik egy téglalap, a másik egy háromszög területét számolja ki. Utána próbáld ki mindkettőt, és írd ki az eredményt.

## Követelmények

1. Hozz létre egy `rectangle_area` nevű függvényt, amely két paramétert kap: a téglalap két oldalát (`a` és `b`). Adja vissza a két oldal szorzatát (`a * b`).

   Függvény:

   ```py
   def függvény_név(paraméter1, paraméter2):
     return paraméter1 * paraméter2
   ```

2. Hozz létre egy `triangle_area` nevű függvényt, amely két paramétert kap: a háromszög alapját (`a`) és magasságát (`m`). Adja vissza az alap és a magasság szorzatának a felét (`a * m / 2`).

   Osztás:

   ```py
   return (szám1 * szám2) / 2
   ```

3. Hívd meg a `rectangle_area` függvényt `2` és `4` értékkel, a `triangle_area` függvényt pedig `2` alappal és `4` magassággal. Írd ki a két eredményt egy sorban, pl. `2*4-es téglalap: 8, 2 alapú, 4 magasságú háromszög: 4.0`.

   Kiírás függvényhívással:

   ```py
   print(f"szöveg: {függvény_név(szám1, szám2)}")
   ```

A függvények tizedes törtekkel (pl. `2.5`) is működjenek, és a háromszög területe lehet nem egész szám is (pl. `triangle_area(3, 5)` → `7.5`). A program semmit ne kérjen be a felhasználótól.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A `rectangle_area` helyesen számolja a téglalap területét (`rectangle_area(2, 4)` → `8`).
- A `triangle_area` helyesen számolja a háromszög területét (`triangle_area(2, 4)` → `4`).
- A `triangle_area` a nem egész eredményt is helyesen adja vissza (`triangle_area(3, 5)` → `7.5`).
- Mindkét függvény működik tizedes törtekkel is.
- A program kiírja mindkét terület értékét.
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
