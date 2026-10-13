# Életkor üzenet

## Feladat

Készíts egy programot, amely megkérdezi a felhasználó életkorát, majd az életkor alapján kiír egy üzenetet: 18 év alatt `Kiskorú vagy`, 18 és 64 év között `Felnőtt vagy`, 65 évtől `Nyugdíjas vagy`.

## Követelmények

1. Kérj be egy egész számot (az életkort), és tárold el egy változóban.

   Beolvasás:

   ```py
   változó = int(input("Kérdés"))
   ```

2. Ellenőrizd először, hogy az életkor kisebb-e 18-nál. Ha igen, írd ki: `Kiskorú vagy`. A `print` szövegét pontosan így add meg.

   Feltétel:

   ```py
   if változó < szám:
     print("szöveg")
   ```

3. Ha az előző feltétel nem teljesült, nézd meg, hogy az életkor kisebb-e 65-nél. Ha igen, írd ki: `Felnőtt vagy`. Ehhez használd az `elif` ágat, amely csak akkor fut le, ha az előző feltétel hamis volt.

   Másik feltétel:

   ```py
   elif változó < szám:
     print("szöveg")
   ```

4. Minden más esetben (65 éves vagy idősebb) írd ki: `Nyugdíjas vagy`. Ehhez használd az `else` ágat.

   Egyéb eset:

   ```py
   else:
     print("szöveg")
   ```

   Példa: a `10` bemenetre a kimenet `Kiskorú vagy`, a `30` bemenetre `Felnőtt vagy`, a `70` bemenetre `Nyugdíjas vagy`.

A program a határértékeknél (`17`, `18`, `64`, `65`) és a `0` bemenetre is helyesen működjön.

## Értékelés

A megoldást 6 teszt ellenőrzi (1-1 pont):

- A program bekéri az életkort (az `input` egyszer meghívódik).
- 18 év alatt (pl. `0`, `10`, `17`) a `Kiskorú vagy` üzenetet írja ki.
- 18 és 64 év között (pl. `30`, `50`) a `Felnőtt vagy` üzenetet írja ki.
- 65 év felett (pl. `70`, `100`) a `Nyugdíjas vagy` üzenetet írja ki.
- A `18` éves már felnőtt.
- A `65` éves már nyugdíjas.

A tesztek az üzenet pontos szövegét ellenőrzik, a kérdés szövegét nem.

## Futtatás

```
python3 main.py
```

## Teszt

```
python3 -m unittest discover -s test -p "test.py" -v
```
