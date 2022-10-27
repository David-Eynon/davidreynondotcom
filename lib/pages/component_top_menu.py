from lib.base_page import BasePage


class ComponentTopMenu(BasePage):

    PROPERTIES_FILE = "component_top_menu.properties"

    def get_about_me_link_top_menu(self, driver):
        return self.get_element(driver, "about_me_link_top_menu")

    def get_linked_in_link_top_menu(self, driver):
        return self.get_element(driver, "linked_in_link_top_menu")

    def get_github_link_top_menu(self, driver):
        return self.get_element(driver, "github_link_top_menu")

    def get_bitbucket_link_top_menu(self, driver):
        return self.get_element(driver, "bitbucket_link_top_menu")

    def get_site_title_banner_top_menu(self, driver):
        return self.get_element(driver, "top_title_name")

    def get_top_menu_banner_text(self, driver):
        return self.get_site_title_banner_top_menu(driver).text

    def get_expected_menu_banner_text(self):
        return self.get_property("expected_top_title_name")