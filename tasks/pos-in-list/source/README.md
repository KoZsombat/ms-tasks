# Elem helye a listában

## Feladat

Készíts egy programot, amely egy számokat tartalmazó listában megkeresi a `3` szám helyét, és kiírja azt.

## Követelmények

1. Hozz létre egy `list` nevű változót, amelybe az `1, 2, 3, 4, 5` számok kerülnek ebben a sorrendben.

   Lista:

   ```py
   változó = [elem1, elem2, elem3]
   ```

2. Keresd meg a `3` szám helyét a listában az `index` függvénnyel. A helyek számozása `0`-tól indul, ezért a `3` helye a `2`.

   Keresés:

   ```py
   változó.index(érték)
   ```

3. Írd ki az eredményt.

   Kiírás:

   ```py
   print(kifejezés)
   ```

   Példa kimenet:

   ```
   2
   ```

A program nem kér be semmit a felhasználótól, és pontosan egy sort ír ki.

## Értékelés

A megoldást 5 teszt ellenőrzi (1-1 pont):

- A `list` változó tartalma `1, 2, 3, 4, 5`.
- A program pontosan egy sort ír ki.
- A program a `3` helyét, vagyis a `2`-t írja ki.
- A kiírt szám megegyezik a `list.index(3)` értékével.
- A program nem használ `input`-ot.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
