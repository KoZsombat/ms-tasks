# Nagyobb szám

## Feladat

Írj egy függvényt, amely két szám közül visszaadja a nagyobbat, majd próbáld ki a `3` és `2` számokkal.

## Követelmények

1. Hozz létre egy `Nagyobb` nevű függvényt, amely két paramétert kap: `a` és `b`.

   Függvény:

   ```py
   def FüggvényNév(paraméter1, paraméter2):
     # ide jön a függvény törzse
   ```

2. A függvényen belül hasonlítsd össze a két számot. Ha `a` a nagyobb, add vissza `a`-t, különben add vissza `b`-t.

   Feltétel és visszatérés:

   ```py
   if (feltétel):
     return érték1
   else:
     return érték2
   ```

3. Hívd meg a függvényt a `3` és `2` számokkal, és írd ki az eredményt. A program kimenete: `3`.

   Függvényhívás és kiírás:

   ```py
   print(FüggvényNév(szám1, szám2))
   ```

A függvény egyenlő számokkal, negatív számokkal és tizedes törtekkel (pl. `2.5`, `2.7`) is működjön.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- Ha az első szám a nagyobb, a függvény azt adja vissza (`Nagyobb(5, 2)` → `5`).
- Ha a második szám a nagyobb, a függvény azt adja vissza (`Nagyobb(2, 7)` → `7`).
- Egyenlő számok esetén a közös értéket adja vissza (`Nagyobb(4, 4)` → `4`).
- Negatív számokat is helyesen hasonlít össze (`Nagyobb(-3, -8)` → `-3`).
- Tizedes törteket is helyesen hasonlít össze (`Nagyobb(2.5, 2.7)` → `2.7`).
- A program kiírja a `3` és `2` közül a nagyobbat.

A kiírás pontos formáját a tesztek nem ellenőrzik, csak azt, hogy a `3` megjelenik-e.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
