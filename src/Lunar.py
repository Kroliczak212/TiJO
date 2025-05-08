class PojazdKsiezycowy:


    def __init__(self, x=0, y=0):

        self._x = x
        self._y = y
        self._kierunek = 0  # 0: Północ, 1: Wschód, 2: Południe, 3: Zachód
        self._wektory = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def ruch_do_przodu(self, kroki=1):

        dx, dy = self._wektory[self._kierunek]
        self._x += dx * kroki
        self._y += dy * kroki
        return self.aktualna_pozycja()

    def ruch_do_tylu(self, kroki=1):

        return self.ruch_do_przodu(-kroki)

    def obrot_w_lewo(self):

        self._kierunek = (self._kierunek - 1) % 4
        return self._kierunek

    def obrot_w_prawo(self):

        self._kierunek = (self._kierunek + 1) % 4
        return self._kierunek

    def aktualna_pozycja(self):

        return (self._x, self._y)

    def aktualny_kierunek(self):

        kierunki = ["N", "E", "S", "W"]
        return kierunki[self._kierunek]
