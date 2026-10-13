# Osztható számok

## Feladat

Készíts egy programot, amely bekér egy számot, majd kiírja az 1 és 100 közötti (a 100-at is beleértve) összes olyan számot, amely osztható a megadott számmal. Minden szám külön sorba kerül.

## Követelmények

1. Kérj be egy pozitív egész számot (az osztót), és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Indíts egy ciklust, amely az 1, 2, ... 100 számokon megy végig. A `range` második száma már nem tartozik bele, ezért 101-et kell megadni.

   Ciklus:

   ```py
   for i in range(1, 101):
     # ismétlődő rész
   ```

3. A cikluson belül ellenőrizd, hogy az `i` osztható-e a beolvasott számmal. A `%` az osztás maradékát adja meg; ha a maradék 0, akkor a szám osztható.

   Feltétel:

   ```py
   if i % változó == 0:
     # ha osztható
   ```

4. Ha osztható, írd ki a számot.

   Kiírás:

   ```py
   print(i)
   ```

   Példa: a `20` bemenetre a kimenet `20`, `40`, `60`, `80`, `100`, mindegyik külön sorban.

A program az `1` (minden számot kiír), a `100` (csak a `100`-at) és a 100-nál nagyobb szám (pl. `101`, ilyenkor nem ír ki semmit) esetén is működjön hibátlanul.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri az osztót (az `input` egyszer meghívódik).
- A `7` többszörösei helyesek.
- A `10` többszörösei helyesek.
- Az `1` esetén az összes szám (1-től 100-ig) megjelenik.
- A `100` esetén a `100` is megjelenik.
- A 100-nál nagyobb osztó esetén nem íródik ki semmi.

A tesztek a kiírt számokat ellenőrzik (soronként egy szám), a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
