from lib.base_test_class import BaseTestClass
from lib.pages.popup_page import PopupPage
from lib.pages.display_pop_up_automation import DisplayPopUpAutomation
import time

class LandingPageTests(BaseTestClass):

    def test_popup_page_is_on_current_page(self):
        popup = PopupPage()
        popup.go_to_page(self.driver)
        self.assertTrue(DisplayPopUpAutomation().is_on_current_page(self.driver))
        