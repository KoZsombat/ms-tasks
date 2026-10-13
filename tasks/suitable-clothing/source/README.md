# Megfelelő ruházat

## Feladat

Készíts egy egyszerű programot, amely bekéri a hőmérsékletet, majd kiírja, hogy milyen ruhát érdemes felvenni.

## Követelmények

1. Kérd be a hőmérsékletet fokban, alakítsd egész számmá, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Vizsgáld meg a hőmérsékletet feltételekkel: először azt, hogy 10 foknál kisebb-e, utána azt, hogy 20 foknál kisebb-e, minden más esetben a hőmérséklet 20 fok vagy több.

   Feltétel:

   ```py
   if változó < szám:
     # teendő
   elif változó < másik_szám:
     # teendő
   else:
     # teendő
   ```

3. Mindhárom esetben írd ki a megfelelő mondatot pontosan így:

   - 10 foknál hidegebb esetén: `Kabátot vegyél fel`
   - 10 foktól 20 fok alatt: `Pulcsit vegyél fel`
   - 20 foktól: `Póló elég`

   Kiírás:

   ```py
   print("szöveg")
   ```

   Példa: a `15` bemenetre a kiírás `Pulcsit vegyél fel`.

A program negatív hőmérséklettel és a határértékekkel (`9`, `10`, `19`, `20`) is működjön hibátlanul.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a hőmérsékletet (az `input` egyszer meghívódik).
- Hideg időben (pl. `5` és `-10` fok) csak a kabátos mondatot írja ki.
- Enyhe időben (pl. `15` fok) csak a pulcsis mondatot írja ki.
- Meleg időben (pl. `25` fok) csak a pólós mondatot írja ki.
- A 10 fokos határnál helyesen dönt (`9` kabát, `10` pulcsi).
- A 20 fokos határnál helyesen dönt (`19` pulcsi, `20` póló).

A tesztek a három kiírt mondat pontos szövegét ellenőrzik, a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
