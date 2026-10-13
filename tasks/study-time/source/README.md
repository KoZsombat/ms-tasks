# Tanulási idő

## Feladat

Készíts egy egyszerű programot, amely tanulási alkalmakat (tantárgy és percek) tárol, és tantárgyanként összeadja a tanulással töltött időt.

## Követelmények

1. Hozz létre egy `sessions` nevű listát. Minden elem egy kételemű lista: az első a tantárgy neve, a második a tanulással töltött percek száma.

   Lista:

   ```py
   sessions = [
     ["Matek", 60],
     ["Történelem", 45],
     ["Matek", 30],
     ["Angol", 50],
     ["Történelem", 20]
   ]
   ```

2. Írj egy `total_time(sessions)` nevű függvényt, amely egy ilyen listát kap, és egy szótárat ad vissza: a kulcs a tantárgy, az érték az összes perc.

   Függvény:

   ```py
   def függvény(lista):
     szótár = {}

     # itt számold ki az összegeket

     return szótár
   ```

3. A függvényben menj végig a lista elemein egy `for` ciklussal. Az elem `[0]` helye a tantárgy, `[1]` helye a percek száma.

   Ciklus:

   ```py
   for elem in lista:
     tantárgy = elem[0]
     percek = elem[1]
   ```

4. Ha a tantárgy már szerepel a szótárban, add hozzá a perceket a meglévő értékhez, különben vedd fel új kulcsként.

   Feltétel:

   ```py
   if tantárgy in szótár:
     szótár[tantárgy] += percek
   else:
     szótár[tantárgy] = percek
   ```

5. Hívd meg a függvényt a `sessions` listával, majd menj végig a kapott szótáron, és minden tantárgynál írj ki egy sort pontosan ebben a formában: `tantárgy: szám perc`. A tantárgyak abban a sorrendben jelenjenek meg, ahogy először előfordulnak a listában.

   Kiírás:

   ```py
   for kulcs in szótár:
     print(f"{kulcs}: {szótár[kulcs]} perc")
   ```

   Példa: a fenti `sessions` listára a kiírás:

   ```
   Matek: 90 perc
   Történelem: 65 perc
   Angol: 50 perc
   ```

A függvény üres listával, egyetlen alkalommal, ékezetes tantárgynévvel és 0 perces alkalommal is működjön hibátlanul.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program a `sessions` listára kiírja a tantárgyankénti összes időt a megadott formában.
- Az ugyanahhoz a tantárgyhoz tartozó alkalmakat összeadja.
- A különböző tantárgyakat külön tartja.
- Egyetlen alkalommal is helyesen működik.
- Üres listára üres szótárat ad vissza.
- Ékezetes tantárgynévvel és 0 perces alkalommal is helyesen működik.

A tesztek a `total_time` függvény nevét, a visszaadott szótár szerkezetét és a kiírt sorok pontos szövegét ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
