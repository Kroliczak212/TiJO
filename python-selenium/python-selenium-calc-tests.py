import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CALC_URL = "https://tgadek.bitbucket.io/app/calc/prod/index.html"

class TestCalculatorDev(unittest.TestCase):
    def setUp(self):
        """
        Inicjalizacja testu - uruchomienie przeglądarki Chrome i otwarcie strony kalkulatora
        """
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(5)
        self.driver.get(CALC_URL)

    def test_tc_01_add_two_negative_numbers(self):
        """
        TC-01: Weryfikacja dodawania liczb ujemnych (-2 + -4 = -6)
        """
        number1 = self.driver.find_element(By.ID, "number1")
        number2 = self.driver.find_element(By.ID, "number2")
        # przycisk Add jako pierwszy input[type='button']
        add_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='button']")

        number1.clear()
        number1.send_keys("-2")
        number2.clear()
        number2.send_keys("-4")
        add_button.click()

        result = self.driver.find_element(By.ID, "result").text
        expected = "-2 + -4 = -6"
        self.assertEqual(result, expected,
                         f"(TC-01) Oczekiwano '{expected}', otrzymano '{result}'")

    def test_tc_02_empty_fields_validation(self):
        """
        TC-02: Weryfikacja komunikatu walidacji przy pustych polach
        """
        number1 = self.driver.find_element(By.ID, "number1")
        number2 = self.driver.find_element(By.ID, "number2")
        add_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='button']")

        # pozostaw pola puste
        number1.clear()
        number2.clear()
        add_button.click()

        result = self.driver.find_element(By.ID, "result").text
        expected_msg = "Formularz zawiera niepoprawne dane!"
        self.assertEqual(result, expected_msg,
                         f"(TC-02) Oczekiwano komunikatu '{expected_msg}', otrzymano '{result}'")

    def tearDown(self):
        """
        Zakończenie testu - zamknięcie przeglądarki
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
