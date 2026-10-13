# Csillagpiramis

## Feladat

Készíts egy programot, amely bekér egy sorszámot, majd annyi soros, középre igazított piramist ír ki `*` karakterekből. Az első sorban 1 csillag van, minden következő sorban kettővel több.

## Követelmények

1. Kérj be egy egész számot (a sorok számát), és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Indíts egy ciklust, amely az 1, 2, ... a sorok számáig megy végig. A `range` második száma már nem tartozik bele, ezért eggyel nagyobbat adj meg. Az `i` mindig az aktuális sor sorszáma.

   Ciklus:

   ```py
   for i in range(1, változó + 1):
     # ismétlődő rész
   ```

3. A cikluson belül számold ki, hány szóköz kell a sor elejére. Az első sorban van a legtöbb, az utolsóban nincs egy sem: ez a sorok száma mínusz `i`. Egy szöveget a `*` jellel meg lehet ismételni: `" " * 3` három szóköz.

   Szóközök:

   ```py
   szóközök = " " * szám
   ```

4. Számold ki, hány csillag kell a sorba: az 1. sorban 1, a 2.-ban 3, a 3.-ban 5, vagyis `2 * i - 1`.

   Csillagok:

   ```py
   csillagok = "*" * szám
   ```

5. Írd ki a szóközöket és a csillagokat egymás után egy sorban.

   Kiírás:

   ```py
   print(szóközök + csillagok)
   ```

   Példa: a `3` bemenetre a kimenet:

   ```
     *
    ***
   *****
   ```

A program az `1`, a `0` (ilyenkor nem ír ki semmit) és nagyobb szám (pl. `12`) esetén is működjön hibátlanul. A sorok végén ne legyen felesleges szóköz.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a sorok számát (az `input` egyszer meghívódik).
- A program pontosan annyi sort ír ki, amennyit kértek.
- A `4` soros piramis helyes, a megadott formában.
- Az `1` soros piramis helyes.
- A `12` soros piramis is helyes.
- A `0` bemenetre nem íródik ki semmi.

A tesztek a sorok pontos formáját ellenőrzik (a szóközöket és a csillagokat), a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
