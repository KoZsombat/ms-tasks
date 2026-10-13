# Kvíz ismétléssel

## Feladat

Készíts egy programot, amely addig kérdezi ugyanazt a kérdést (`Mennyi 7 * 8?`), amíg a felhasználó meg nem adja a helyes választ (`56`). Ha a válasz rossz, a program szól, és újra rákérdez; a helyes válasz után gratulál.

## Követelmények

1. Kérd be a felhasználó első válaszát, és tárold el egy változóban. A válasz szöveg marad, nem kell számmá alakítani.

   Beolvasás:

   ```py
   változó = input("Kérdés")
   ```

2. Indíts egy ciklust, amely addig fut, amíg a válasz nem egyezik a helyes megoldással (`"56"`).

   Ciklus:

   ```py
   while változó != "szöveg":
     # ismétlődő rész
   ```

3. A cikluson belül írd ki, hogy a válasz rossz, majd kérd be újra a választ ugyanabba a változóba.

   Kiírás és újra beolvasás:

   ```py
   print("szöveg")
   változó = input("Kérdés")
   ```

4. A ciklus után (vagyis amikor a válasz helyes) írj ki egy gratuláló üzenetet.

   Kiírás:

   ```py
   print("szöveg")
   ```

   Példa: a `10`, majd az `56` válaszokra a program kétszer kérdez, egyszer jelzi a hibát, a végén pedig kiírja, hogy helyes a válasz.

A program üres és ékezetes válasz esetén is rossznak vegye a választ, és hiba nélkül kérdezzen tovább.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- Helyes első válasznál az `input` csak egyszer hívódik meg.
- Helyes válasz után a program kiír egy üzenetet.
- Rossz válasz után a program újra rákérdez.
- A program addig kérdez, amíg helyes választ nem kap (több rossz válasz után is).
- A helyes válasz után a program már nem kérdez tovább.
- Az üres és az ékezetes válasz is rossz válasznak számít, és nem okoz hibát.

A tesztek a kérdések számát ellenőrzik, a kérdés és az üzenetek szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
