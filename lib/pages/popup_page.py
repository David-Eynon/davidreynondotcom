from lib.base_page import BasePage


class PopupPage(BasePage):

    PROPERTIES_FILE = "popup_page.properties"

    def get_page_text(self, driver):
        return self.get_element(driver,'page_text').text

    def get_expected_page_text(self):
        return self.get_property('expected_page_text')    