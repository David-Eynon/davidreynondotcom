from lib.base_test_class import BaseTestClass
from lib.pages.component_top_menu import ComponentTopMenu
from lib.pages.home_page import HomePage
import time

class InitialTestTests(BaseTestClass):

    def test_landing_page_is_on_current_page(self):
        home_page = HomePage()
        top_menu = ComponentTopMenu()
        home_page.go_to_page(self.driver)
        banner_txt = top_menu.get_top_menu_banner_text(self.driver)
        expected = top_menu.get_expected_menu_banner_text()
        self.assertEqual(banner_txt, expected)

