from lib.base_test_class import BaseTestClass
from lib.pages.olympic_page import OlympicPage
from lib.pages.display_pytwitservice import DisplayPytwitservice
import time

class LandingPageTests(BaseTestClass):

    def test_olympic_page_is_on_current_page(self):
        """
        Test page that initially appears is olympic page
        """
        olympic = OlympicPage()
        olympic.go_to_page(self.driver)
        self.assertTrue(DisplayPytwitservice().is_on_current_page(self.driver))