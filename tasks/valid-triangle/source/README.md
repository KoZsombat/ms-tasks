# Valódi háromszög

## Feladat

Készíts egy egyszerű programot, amely bekéri egy háromszög három oldalának hosszát, majd kiírja, hogy az oldalakból szerkeszthető-e valódi háromszög.

## Követelmények

1. Kérd be az első oldal hosszát, alakítsd egész számmá, és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Ugyanígy kérd be a második és a harmadik oldal hosszát is, külön változókba.

3. Döntsd el, hogy valódi háromszög-e. Az oldalakból akkor szerkeszthető háromszög, ha bármely két oldal összege **nagyobb** a harmadik oldalnál (mindhárom párosításra igaznak kell lennie). A feltételeket az `and` (és) köti össze.

   Feltétel:

   ```py
   if (a + b > c and a + c > b and b + c > a):
     # teendő
   else:
     # teendő
   ```

4. Írd ki a megfelelő mondatot pontosan így:

   - valódi háromszög esetén: `Valódi háromszög`
   - ha nem valódi háromszög: `Nem valódi háromszög`

   Kiírás:

   ```py
   print("szöveg")
   ```

   Példa: a `3`, `4`, `5` bemenetre a kiírás `Valódi háromszög`, az `1`, `2`, `3` bemenetre `Nem valódi háromszög`.

A program akkor is működjön helyesen, ha két oldal összege pontosan egyenlő a harmadikkal (pl. `1`, `2`, `3`), ha az egyik oldal nulla, és bármilyen sorrendben adják meg az oldalakat.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program három oldalt kér be (az `input` háromszor hívódik meg).
- A valódi háromszögeket (pl. `3`, `4`, `5`) felismeri.
- Ha az egyik oldal túl hosszú (pl. `1`, `1`, `5`), nem valódi háromszöget jelez.
- Ha két oldal összege egyenlő a harmadikkal (pl. `1`, `2`, `3`), nem valódi háromszöget jelez.
- Az oldalak sorrendje nem számít.
- Ha az egyik oldal nulla, nem valódi háromszöget jelez.

A tesztek a két kiírt mondat pontos szövegét ellenőrzik, a kérdések szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
