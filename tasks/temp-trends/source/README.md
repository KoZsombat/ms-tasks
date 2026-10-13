# Hőmérséklet-trendek

## Feladat

Készíts egy egyszerű programot, amely egy lista napi hőmérsékleteiből megszámolja, hány napon emelkedett, csökkent vagy maradt ugyanannyi a hőmérséklet az előző naphoz képest.

## Követelmények

1. Hozz létre egy `temps` nevű listát a napi hőmérsékletekkel:

   ```py
   temps = [12, 14, 15, 15, 13, 11, 11, 16, 18, 17]
   ```

2. Írj egy `trends` nevű függvényt, amely egy hőmérséklet-listát kap paraméterként.

   Függvény:

   ```py
   def trends(lista):
     # a függvény teste
   ```

3. A függvényben vezess három számlálót, mindegyik 0-ról induljon.

   Változók:

   ```py
   számláló = 0
   ```

4. Menj végig a lista elemein a második naptól kezdve, és hasonlítsd össze mindegyiket az előző nappal. A `lista[i]` az aktuális, a `lista[i - 1]` az előző nap hőmérséklete.

   Ciklus és feltétel:

   ```py
   for i in range(1, len(lista)):
     if lista[i] > lista[i - 1]:
       # teendő
     elif lista[i] < lista[i - 1]:
       # teendő
     else:
       # teendő
   ```

5. A függvény adja vissza sorrendben az emelkedő, a csökkenő és a változatlan napok számát.

   Visszatérés:

   ```py
   return első, második, harmadik
   ```

6. Hívd meg a függvényt a `temps` listával, és írd ki az eredményt pontosan ebben a formában.

   Kiírás:

   ```py
   print(f"Emelkedő napok: {változó}")
   ```

   Példa: a fenti `temps` listára a kiírás:

   ```
   Emelkedő napok: 4
   Csökkenő napok: 3
   Változatlan napok: 2
   ```

A függvény üres listával és egyelemű listával is működjön hibátlanul (mindhárom szám ilyenkor 0).

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program a `temps` listára kiírja a három számot a megadott formában.
- Végig emelkedő hőmérsékleteknél (pl. `[1, 2, 3, 4]`) a `trends` helyesen számol.
- Végig csökkenő hőmérsékleteknél (pl. `[4, 3, 2, 1]`) a `trends` helyesen számol.
- Egyforma hőmérsékleteknél (pl. `[5, 5, 5]`) a `trends` helyesen számol.
- Vegyes hőmérsékleteknél a `trends` helyesen számol.
- Üres és egyelemű listánál a `trends` mindhárom értéke 0.

A tesztek a `trends` függvény nevét és a visszaadott értékek sorrendjét (emelkedő, csökkenő, változatlan), valamint a kiírt három sor pontos szövegét ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
