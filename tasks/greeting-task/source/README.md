# Köszönés

## Feladat

Készíts egy egyszerű programot, amely megkérdezi a felhasználó nevét, majd köszön neki.

## Követelmények

1. Kérj be a felhasználótól egy nevet, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = input("Kérdés")
   ```

2. Köszönj a felhasználónak: írd ki a beolvasott nevet egy üdvözlő szövegben, pl. `Szia Zsombor!`.

   Kiírás:

   ```py
   print(f"szöveg {változó}")
   ```

A program ékezetes névvel (pl. `Árvíztűrő`) és üres névvel is működjön hiba nélkül.

## Értékelés

A megoldást 4 teszt ellenőrzi (1-1 pont):

- A program bekéri a nevet (az `input` egyszer meghívódik).
- A program kiírja a beolvasott nevet.
- Az ékezetes nevet is helyesen írja ki.
- Üres név esetén is lefut, és kiír egy sort.

A kérdés és az üdvözlés pontos szövegét a tesztek nem ellenőrzik.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
