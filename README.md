# chmod konwerter

Ten projekt implementuje konwerter trybów dostępu do plików w systemie Unix/Linux, umożliwiający konwersję między notacją symboliczną a numeryczną.

## Opis problemu

W systemach Unix/Linux, uprawnienia dostępu do plików i katalogów mogą być reprezentowane na dwa sposoby:
1. Notacja symboliczna (np. `rwxr-xr-x`)
2. Notacja numeryczna (np. `755`)

Celem tego projektu jest stworzenie narzędzia, które umożliwia łatwą konwersję między tymi dwoma sposobami.

## Struktura projektu

- `chmodconverter_functions.py`: Zawiera główne funkcje konwertujące
- `chmodconverter.py`: Implementacja interfejsu wiersza poleceń
- `chmodconverter_gui.py`: Implementacja interfejsu graficznego
- `test.py`: Testy jednostkowe dla funkcji konwertujących

## Jak uruchomić

### Interfejs wiersza poleceń

```bash
python chmodconverter.py -s rwxr-xr-x  # Konwersja z notacji symbolicznej na numeryczną
python chmodconverter.py -n 755        # Konwersja z notacji numerycznej na symboliczną
```

### Interfejs graficzny

```bash
python chmodconverter_gui.py
```

## Testy

Aby uruchomić testy jednostkowe:

```bash
python -m unittest test.py
```
