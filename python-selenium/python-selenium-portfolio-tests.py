import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://tgadek.bitbucket.io/app/portfolio/prod/"
PAGES = ["index.html", "portfolio.html", "team.html", "experience.html"]
EXPECTED_FOOTER = "© 2024 IT Design. Wszystkie prawa zastrzeżone."

class TestPortfolioDev(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(5)

    def test_uc_01_intro_header_text(self):
        """
        UC-01: Nagłówek <h2> nad sekcją .intro w index.html powinien brzmieć:
        'Profesjonalne Rozwiązania IT dla Twojej Firmy'
        """
        self.driver.get(BASE_URL + "index.html")
        # Pierwszy <h2> wewnątrz kontenera przed .intro
        intro_header = self.driver.find_element(By.XPATH, "//div[@class='container']/h2").text
        expected = "Profesjonalne Rozwiązania IT dla Twojej Firmy"
        self.assertEqual(intro_header, expected,
                         f"(UC-01) Oczekiwano '{expected}', otrzymano '{intro_header}'")

    def test_uc_02_portfolio_header(self):
        """
        UC-02: Nagłówek <h1> w portfolio.html obok logo powinien zawierać 'IT Design'
        """
        self.driver.get(BASE_URL + "portfolio.html")
        header_text = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(header_text, "IT Design",
                         f"(UC-02) Oczekiwano 'IT Design', otrzymano '{header_text}'")

    def test_uc_03_team_images_load(self):
        """
        UC-03: Obrazy na team.html powinny się ładować poprawnie.
        """
        self.driver.get(BASE_URL + "team.html")
        imgs = self.driver.find_elements(By.CSS_SELECTOR, ".team-member img")
        for img in imgs:
            # check naturalWidth > 0
            loaded = self.driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0;",
                img
            )
            alt = img.get_attribute("alt")
            self.assertTrue(loaded, f"(UC-03) Obrazek '{alt}' nie załadował się poprawnie")

    def test_uc_04_experience_paragraph_style(self):
        """
        UC-04: Wszystkie akapity w experience.html mają spójny styl (brak inline font-size).
        """
        self.driver.get(BASE_URL + "experience.html")
        paras = self.driver.find_elements(By.CSS_SELECTOR, ".experience p")
        for p in paras:
            style = p.get_attribute("style") or ""
            self.assertFalse("font-size" in style,
                             f"(UC-04) Nieoczekiwany inline style w paragrafie: '{style}'")

    def test_uc_05_footer_year_consistency(self):
        """
        UC-05: Stopka na każdej stronie powinna zawierać aktualny rok 2024.
        """
        for page in PAGES:
            with self.subTest(page=page):
                self.driver.get(BASE_URL + page)
                footer_text = self.driver.find_element(By.CSS_SELECTOR, "footer p").text
                self.assertEqual(footer_text, EXPECTED_FOOTER,
                                 f"(UC-05:{page}) Oczekiwano '{EXPECTED_FOOTER}', otrzymano '{footer_text}'")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
