from lib.base_test_class import BaseTestClass
from lib.pages.popup_page import PopupPage
import time

class LandingPageTests(BaseTestClass):

    def test_popup_page_is_on_current_page(self):
        popup = PopupPage()
        popup.go_to_page(self.driver)
        page_text = popup.get_page_text(self.driver)
        expected_text = popup.get_expected_page_text()
        self.assertEqual(page_text, expected_text)
        