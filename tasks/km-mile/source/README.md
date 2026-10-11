# Kilométer és mérföld

## Feladat

Írj két függvényt, amelyek kilométert mérföldre, illetve mérföldet kilométerre váltanak át. Utána próbáld ki mindkettőt 1-gyel, és írd ki az eredményt.

## Követelmények

1. Hozz létre egy `km_mile` nevű függvényt, amely egy paramétert kap: a távolságot kilométerben (`km`). Adja vissza a távolságot mérföldben: ehhez szorozd meg `0.62`-vel.

   Függvény:

   ```py
   def függvény_név(paraméter):
     return paraméter * szám
   ```

2. Hozz létre egy `mile_km` nevű függvényt, amely egy paramétert kap: a távolságot mérföldben (`mile`). Adja vissza a távolságot kilométerben: ehhez szorozd meg `1.609`-cel.

3. Hívd meg mindkét függvényt `1`-gyel, és írd ki a két eredményt egy sorban, pl. `1 mérföld: 1.609 km, 1 kilométer: 0.62 mérföld.`

   Kiírás függvényhívással:

   ```py
   print(f"szöveg: {függvény_név(szám)}")
   ```

A függvények `0`-val és tizedes törtekkel (pl. `2.5`) is működjenek. A program semmit ne kérjen be a felhasználótól.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A `km_mile` helyesen váltja át a kilométert mérföldre (`km_mile(1)` → kb. `0.62`).
- A `mile_km` helyesen váltja át a mérföldet kilométerre (`mile_km(1)` → kb. `1.609`).
- A `0` távolság mindkét irányban `0`.
- A tizedes törteket is helyesen váltja át.
- A program kiírja mindkét átváltás eredményét.
- A program nem kér be adatot (`input` nem hívódik meg).

Az eredményeknek 1%-on belül kell lenniük a pontos értéktől, így a `0.621`-es szorzó is elfogadott. A kiírt szöveg pontos megfogalmazását a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
