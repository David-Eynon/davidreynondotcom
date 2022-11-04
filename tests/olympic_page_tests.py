from lib.base_test_class import BaseTestClass
from lib.pages.olympic_page import OlympicPage
import time

class LandingPageTests(BaseTestClass):

    def test_olympic_page_is_on_current_page(self):
        olympic = OlympicPage()
        olympic.go_to_page(self.driver)
        page_text = olympic.get_page_text(self.driver)
        expected_text = olympic.get_expected_page_text()
        self.assertEqual(page_text, expected_text)
