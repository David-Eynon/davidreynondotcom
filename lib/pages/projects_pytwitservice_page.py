from lib.base_page import BasePage

class ProjectsPyTwitServicePage(BasePage):

    PROPERTIES_FILE = "projects_pytwitservice_page.properties"

    """ 
    Note: This is functioning as a standalone page for now, thus the full url and 
    the direct navigation pre-test
    """

    def get_page_title(self, driver) -> str:
        return self.get_element(driver, "page_title").text

    def get_expected_page_title(self) -> str:
        return self.get_property("expected_page_title")
