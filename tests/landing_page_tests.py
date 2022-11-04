from lib.base_test_class import BaseTestClass
from lib.pages.component_top_menu import ComponentTopMenu
from lib.pages.component_bottom_menu import ComponentBottomMenu
from lib.pages.component_display_container import ComponentDisplayContainer
from lib.pages.home_page import HomePage
import time

class LandingPageTests(BaseTestClass):

    def test_refactor_base_url(self):
        home_page = HomePage()
        home_page.go_to_page(self.driver)


    def test_landing_page_about_me_display_component_elements_loaded_as_expected(self):
        home_page = HomePage()
        home_page.go_to_page(self.driver)
        display = ComponentDisplayContainer()
        display_text = display.get_display_container_project_name(self.driver).text
        self.assertEqual(display_text, 'ABOUT ME')
        # no exceptions == implicit pass
        display.get_display_container_content_image(self.driver)
        display.get_display_container_content_long_description(self.driver)
        display.get_display_container_content_long_description2(self.driver)
        display.get_display_container_content_long_description3(self.driver)
        display.get_display_container_content_long_description4(self.driver)
        display.get_display_container_content_project_url(self.driver)
        display.get_display_container_content_project_keywords(self.driver)

    def test_landing_page_is_on_current_page(self):
        home_page = HomePage()
        top_menu = ComponentTopMenu()
        home_page.go_to_page(self.driver)
        banner_txt = top_menu.get_top_menu_banner_text(self.driver)
        expected = top_menu.get_expected_menu_banner_text()
        self.assertEqual(banner_txt, expected)

    def test_landing_page_top_menu_about_me_link_href(self):
        home_page = HomePage()
        top_menu = ComponentTopMenu()
        home_page.go_to_page(self.driver)
        aboutme_link = top_menu.get_about_me_link_top_menu(self.driver).get_attribute('href')
        expected = top_menu.get_expected_about_me_link_href()
        self.assertEqual(aboutme_link, expected)

    def test_landing_page_top_menu_linked_in_link_href(self):
        home_page = HomePage()
        top_menu = ComponentTopMenu()
        home_page.go_to_page(self.driver)
        linkedin_link = top_menu.get_linked_in_link_top_menu(self.driver).get_attribute('href')
        expected = top_menu.get_expected_linked_in_link_href()
        self.assertEqual(linkedin_link, expected)

    def test_landing_page_top_menu_github_link_href(self):
        home_page = HomePage()
        top_menu = ComponentTopMenu()
        home_page.go_to_page(self.driver)
        github_link = top_menu.get_github_link_top_menu(self.driver).get_attribute('href')
        expected = top_menu.get_expected_github_link_href()
        self.assertEqual(github_link, expected)

    def test_landing_page_top_menu_bitbucket_link_href(self):
        home_page = HomePage()
        top_menu = ComponentTopMenu()
        home_page.go_to_page(self.driver)
        bitbucket_link = top_menu.get_bitbucket_link_top_menu(self.driver).get_attribute('href')
        expected = top_menu.get_expected_bitbucket_link_href()
        self.assertEqual(bitbucket_link, expected)

    def test_landing_page_bottom_menu_about_me_link_href(self):
        home_page = HomePage()
        bottom_menu = ComponentBottomMenu()
        home_page.go_to_page(self.driver)
        aboutme_link = bottom_menu.get_about_me_link_bottom_menu(self.driver).get_attribute('href')
        expected = bottom_menu.get_expected_about_me_link_href()
        self.assertEqual(aboutme_link, expected)

    def test_landing_page_bottom_menu_linked_in_link_href(self):
        home_page = HomePage()
        bottom_menu = ComponentBottomMenu()
        home_page.go_to_page(self.driver)
        linkedin_link = bottom_menu.get_linked_in_link_bottom_menu(self.driver).get_attribute('href')
        expected = bottom_menu.get_expected_linked_in_link_href()
        self.assertEqual(linkedin_link, expected)

    def test_landing_page_bottom_menu_github_link_href(self):
        home_page = HomePage()
        bottom_menu = ComponentBottomMenu()
        home_page.go_to_page(self.driver)
        github_link = bottom_menu.get_github_link_bottom_menu(self.driver).get_attribute('href')
        expected = bottom_menu.get_expected_github_link_href()
        self.assertEqual(github_link, expected)

    def test_landing_page_bottom_menu_bitbucket_link_href(self):
        home_page = HomePage()
        bottom_menu = ComponentBottomMenu()
        home_page.go_to_page(self.driver)
        bitbucket_link = bottom_menu.get_bitbucket_link_bottom_menu(self.driver).get_attribute('href')
        expected = bottom_menu.get_expected_bitbucket_link_href()
        self.assertEqual(bitbucket_link, expected)        
