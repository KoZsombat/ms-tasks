# Telefonkönyv

## Feladat

Készíts egy egyszerű telefonkönyvet, amely névjegyeket (név és telefonszám) tárol, és a felhasználó név alapján rákereshet egy névjegyre.

## Követelmények

1. Hozz létre egy `contacts` nevű szótárat: a kulcs a név, az érték a telefonszám (szövegként).

   Szótár:

   ```py
   contacts = {
     "Anna": "+36301234567",
     "Bence": "+36207654321",
     "Árpád": "+36701112233"
   }
   ```

2. Írj egy `find_contact(contacts, name)` nevű függvényt (a paraméterek sorrendje ez legyen). Ha a név szerepel a szótárban, adja vissza a hozzá tartozó telefonszámot, különben adjon vissza `None`-t.

   Függvény és feltétel:

   ```py
   def függvény(szótár, kulcs):
     if kulcs in szótár:
       return szótár[kulcs]

     return None
   ```

3. Kérd be a keresett nevet, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = input("Kérdés")
   ```

4. Hívd meg a függvényt a beolvasott névvel, és az eredményt tárold el egy másik változóban.

   Függvényhívás:

   ```py
   eredmény = függvény(szótár, változó)
   ```

5. Ha az eredmény `None`, írd ki pontosan, hogy `Nincs ilyen névjegy`. Különben írd ki pontosan ebben a formában: `név telefonszáma: szám`.

   Feltétel és kiírás:

   ```py
   if eredmény is None:
     print("szöveg")
   else:
     print(f"{változó} telefonszáma: {eredmény}")
   ```

   Példa: az `Anna` bemenetre a kiírás `Anna telefonszáma: +36301234567`, a `Béla` bemenetre `Nincs ilyen névjegy`.

A keresés ékezetes névvel (pl. `Árpád`), ismeretlen névvel, üres névvel is működjön hibátlanul. A keresés megkülönbözteti a kis- és nagybetűt (az `anna` nem találja meg az `Anna` névjegyet).

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri a keresett nevet (az `input` egyszer meghívódik).
- Létező névjegyet megtalál (pl. `Anna`).
- Egy másik létező névjegyet is megtalál (pl. `Bence`).
- Az ékezetes nevű névjegyet is megtalálja (`Árpád`).
- Ismeretlen, üres és eltérő kis-nagybetűs név esetén kiírja, hogy `Nincs ilyen névjegy`.
- A `find_contact` függvény a számot adja vissza, ismeretlen névnél pedig `None`-t.

A tesztek a kiírt mondatok pontos szövegét ellenőrzik, a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
