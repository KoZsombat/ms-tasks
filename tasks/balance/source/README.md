# Megmaradt pénz

## Feladat

Készíts egy egyszerű programot, amely bekéri, mennyi pénzt kerestél, majd addig kéri a kiadásaidat, amíg `0`-t nem adsz meg. Végül kiírja, mennyi pénzed maradt.

## Követelmények

1. Kérd be a bevételt, alakítsd egész számmá, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Kérd be az első kiadást is egész számként egy másik változóba, és hozz létre egy összegző változót `0` kezdőértékkel.

   Összegző változó:

   ```py
   összeg = 0
   ```

3. Indíts egy ciklust, amely addig ismétlődik, amíg a beolvasott kiadás nem `0`.

   Ciklus:

   ```py
   while változó != 0:
     # ismétlődő rész
   ```

4. A cikluson belül először add hozzá az aktuális kiadást az összeghez, utána kérd be a következő kiadást.

   Hozzáadás:

   ```py
   összeg += változó
   ```

5. A ciklus után számold ki a megmaradt pénzt: vond ki az összes kiadást a bevételből, és írd ki az eredményt, pl. `1000` bevétel, `300` és `200` kiadás, majd `0` esetén a kiírásban szerepeljen az `500`.

   Kiírás:

   ```py
   print(f"szöveg {változó1 - változó2}")
   ```

A program akkor is működjön, ha csak egy kiadás van, ha rögtön `0`-t adsz meg (nincs kiadás), ha többet költöttél, mint amennyit kerestél (az eredmény negatív szám, pl. `-50`), és nagy számokkal is.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program addig kéri a kiadásokat, amíg `0`-t nem kap (pl. a bevétel és három beolvasás: az `input` négyszer hívódik meg).
- Több kiadást is helyesen összead (pl. 1000 bevétel, 300 és 200 kiadás esetén 500).
- Egyetlen kiadást is beszámít (pl. 1000 bevétel és 300 kiadás esetén 700).
- Kiadás nélkül (rögtön `0`) az eredmény a bevétel.
- Ha többet költöttél, mint amennyit kerestél, az eredmény negatív szám (pl. 100 bevétel, 60 és 90 kiadás esetén -50).
- Nagy számoknál is helyes az eredmény.

A kérdések és a kiírás pontos szövegét a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
