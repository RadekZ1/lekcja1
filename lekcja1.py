class Film:
    def __init__(self):
        self._tytul = ""
        self._liczba_wypozyczen = 0


    def set_tytul(self, tytul):
        if len(tytul) <= 20:
            self._tytul = tytul
        else:
            print("Tytuł nie może przekraczać 20 znaków.")


    def get_tytul(self):
        return self._tytul

    def get_liczba_wypozyczen(self):
        return self._liczba_wypozyczen

    def inkrementuj_wypozyczenia(self):
        self._liczba_wypozyczen += 1

film = Film()
print("Początkowy tytuł filmu:", film.get_tytul())
print("Początkowa liczba wypożyczeń:", film.get_liczba_wypozyczen())

film.set_tytul("Incepcja")
print("\nPo ustawieniu tytułu filmu na 'Incepcja':", film.get_tytul())

tytul_filmu = film.get_tytul()
print("\nPobrany tytuł filmu:", tytul_filmu)

print("\nLiczba wypożyczeń przed inkrementacją:", film.get_liczba_wypozyczen())
film.inkrementuj_wypozyczenia()
print("Liczba wypożyczeń po inkrementacji:", film.get_liczba_wypozyczen())
