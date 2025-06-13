import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """
        Inicjalizacja testu - uruchomienie przeglądarki Chrome i otwarcie strony kalkulatora
        """
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')

    def test_addition(self):
        """
        Test sprawdzający działanie operacji dodawania w kalkulatorze
        """
        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("1")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("2")

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "1 + 2 = 3")

    def tearDown(self):
        """
        Zakończenie testu - zamknięcie przeglądarki
        """
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
