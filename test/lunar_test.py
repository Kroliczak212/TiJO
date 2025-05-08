import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Lunar import PojazdKsiezycowy

class TestPojazdKsiezycowy(unittest.TestCase):
    def setUp(self):
        self.pojazd = PojazdKsiezycowy()

    def test_poczatkowa_pozycja(self):
        self.assertEqual(self.pojazd.aktualna_pozycja(), (0, 0))
        self.assertEqual(self.pojazd.aktualny_kierunek(), "N")

    def test_ruch_do_przodu(self):
        self.pojazd.ruch_do_przodu(3)
        self.assertEqual(self.pojazd.aktualna_pozycja(), (0, 3))

    def test_ruch_do_tylu(self):
        self.pojazd.ruch_do_tylu(2)
        self.assertEqual(self.pojazd.aktualna_pozycja(), (0, -2))

    def test_obroty_w_prawo(self):
        self.assertEqual(self.pojazd.obrot_w_prawo(), 1)
        self.assertEqual(self.pojazd.obrot_w_prawo(), 2)
        self.assertEqual(self.pojazd.obrot_w_prawo(), 3)
        self.assertEqual(self.pojazd.obrot_w_prawo(), 0)

    def test_obroty_w_lewo(self):
        self.assertEqual(self.pojazd.obrot_w_lewo(), 3)
        self.assertEqual(self.pojazd.obrot_w_lewo(), 2)
        self.assertEqual(self.pojazd.obrot_w_lewo(), 1)
        self.assertEqual(self.pojazd.obrot_w_lewo(), 0)

    def test_zlozony_ruch(self):
        self.pojazd.ruch_do_przodu()          # (0,1)
        self.pojazd.obrot_w_prawo()           # E
        self.pojazd.ruch_do_przodu(2)        # (2,1)
        self.pojazd.obrot_w_lewo()            # N
        self.pojazd.ruch_do_tylu()            # (2,0)

        self.assertEqual(self.pojazd.aktualna_pozycja(), (2, 0))
        self.assertEqual(self.pojazd.aktualny_kierunek(), "N")

if __name__ == '__main__':
    unittest.main()
