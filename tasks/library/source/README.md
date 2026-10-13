# Könyvtár

## Feladat

Készíts egy egyszerű programot, amely nyilvántartja egy könyvtár könyveit, és kezeli a kölcsönzést és a visszavételt.

## Követelmények

1. Hozz létre egy `books` nevű szótárat: a kulcs a könyv címe, az érték annak a neve, aki kikölcsönözte. Az üres szöveg (`""`) azt jelenti, hogy a könyv szabad.

   Szótár:

   ```py
   books = {
     "Egri csillagok": "",
     "A Pál utcai fiúk": "",
     "Légy jó mindhalálig": ""
   }
   ```

2. Írj egy `borrow_book(books, title, name)` nevű függvényt (a paraméterek sorrendje ez legyen). Ha a könyv nincs a szótárban, vagy már ki van kölcsönözve, adjon vissza `False`-t. Különben írja be a nevet a könyv mellé, és adjon vissza `True`-t.

   Függvény és feltétel:

   ```py
   def függvény(szótár, kulcs, érték):
     if kulcs not in szótár or szótár[kulcs] != "":
       return False

     szótár[kulcs] = érték
     return True
   ```

3. Írj egy `return_book(books, title)` nevű függvényt. Ha a könyv nincs a szótárban, vagy nincs kikölcsönözve, adjon vissza `False`-t. Különben állítsa vissza az értéket üres szövegre, és adjon vissza `True`-t.

4. Hívd meg a függvényeket, és írd ki az eredményüket, ebben a sorrendben:

   - `borrow_book(books, "Egri csillagok", "Anna")`
   - `borrow_book(books, "Egri csillagok", "Bence")`
   - `return_book(books, "Egri csillagok")`
   - `return_book(books, "Egri csillagok")`

   Kiírás:

   ```py
   print(függvény(szótár, "cím", "név"))
   ```

5. Ezután kölcsönözd ki a `"A Pál utcai fiúk"` könyvet `"Bence"` nevére (kiírás nélkül).

6. Menj végig a könyveken egy `for` ciklussal, és minden könyvnél írj ki egy sort pontosan ebben a formában:

   - szabad könyv: `cím: szabad`
   - kikölcsönzött könyv: `cím: név kölcsönözte ki`

   Ciklus:

   ```py
   for kulcs in szótár:
     # a szótár értéke: szótár[kulcs]
   ```

   Példa: a teljes kimenet

   ```
   True
   False
   True
   False
   Egri csillagok: szabad
   A Pál utcai fiúk: Bence kölcsönözte ki
   Légy jó mindhalálig: szabad
   ```

A függvények ismeretlen könyvvel, már kikölcsönzött könyvvel és nem kikölcsönzött könyv visszavételével is működjenek helyesen.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program a fenti példa szerint kiírja a műveletek eredményét és a könyvek állapotát.
- A szabad könyvet ki lehet kölcsönözni (`True`, a név bekerül a szótárba).
- A már kikölcsönzött könyvet nem lehet újra kikölcsönözni (`False`, a szótár nem változik).
- Ismeretlen könyvet nem lehet kikölcsönözni (`False`, a szótár nem változik).
- A kikölcsönzött könyvet vissza lehet venni (`True`, az érték újra üres szöveg).
- A szabad vagy ismeretlen könyvet nem lehet visszavenni (`False`, a szótár nem változik).

A tesztek a függvények nevét, a paraméterek sorrendjét, a visszaadott `True`/`False` értékeket és a kiírt sorok pontos szövegét ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
