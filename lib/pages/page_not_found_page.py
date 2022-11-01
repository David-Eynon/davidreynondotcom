from lib.base_page import BasePage

class PageNotFoundPage(BasePage):

    PROPERTIES_FILE = "page_not_found_page.properties"

    def get_page_title(self, driver):
        return self.get_element(driver,'page_not_found_title').text

    def get_page_status(self, driver):
        return self.get_element(driver, 'page_not_found_status').text    

    def get_expected_page_title(self):
        return self.get_property('expected_page_title')

    def get_expected_page_status(self):
        return self.get_property('expected_page_status')        