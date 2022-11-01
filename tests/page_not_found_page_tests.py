from lib.base_test_class import BaseTestClass
from lib.pages.home_page import HomePage
from lib.pages.page_not_found_page import PageNotFoundPage
import time

class PageNotFoundPageTests(BaseTestClass):
    
    def test_page_not_found_is_on_current_page(self):
        homepage = HomePage()
        homepage.go_to_page(self.driver)
        not_found = PageNotFoundPage()
        # refactor this later. 
        # This could be solved with issue https://github.com/drocpdp/test_framework_template/issues/4
        this_url = self.driver.current_url
        self.driver.get(this_url + '/afseaf')
        page_title = not_found.get_page_title(self.driver)
        expected = not_found.get_expected_page_title()
        self.assertEqual(page_title, expected)
        page_status = not_found.get_page_status(self.driver)
        expected = not_found.get_expected_page_status()
        self.assertEqual(page_status, expected)