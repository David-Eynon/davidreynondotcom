from lib.base_page import BasePage


class ComponentBottomMenu(BasePage):

    PROPERTIES_FILE = "component_bottom_menu.properties"

    def get_about_me_link_bottom_menu(self, driver):
        return self.get_element(driver, "about_me_link_bottom_menu")

    def get_linked_in_link_bottom_menu(self, driver):
        return self.get_element(driver, "linked_in_link_bottom_menu")

    def get_github_link_bottom_menu(self, driver):
        return self.get_element(driver, "github_link_bottom_menu")

    def get_bitbucket_link_bottom_menu(self, driver):
        return self.get_element(driver, "bitbucket_link_bottom_menu")

    def get_site_title_banner_bottom_menu(self, driver):
        return self.get_element(driver, "bottom_title_name")

    def get_bottom_menu_banner_text(self, driver):
        return self.get_site_title_banner_bottom_menu(driver).text

    def get_expected_menu_banner_text(self):
        return self.get_property("expected_bottom_title_name")

    def get_expected_about_me_link_href(self):
        return self.get_base_site_url() + self.get_property("expected_about_me_link_href")

    def get_expected_linked_in_link_href(self):
        return self.get_property("expected_linkedin_link_href")

    def get_expected_github_link_href(self):
        return self.get_property("expected_github_link_href")

    def get_expected_bitbucket_link_href(self):
        return self.get_property("expected_bitbucket_link_href")

    def get_copyright_year_bottom_menu_text(self, driver):
        return self.get_element(driver, "copyright_year_bottom_menu").text