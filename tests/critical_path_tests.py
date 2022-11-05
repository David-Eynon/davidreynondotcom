import time
from lib.base_test_class import BaseTestClass
from lib.pages.home_page import HomePage
from lib.pages.component_project_cards import ComponentProjectCards
from lib.pages.display_angular_resume_site import DisplayAngularResumeSite
from lib.pages.display_pop_up_automation import DisplayPopUpAutomation
from lib.pages.display_pytwitservice import DisplayPytwitservice
from lib.pages.display_testing_davidreynondotcom import DisplayTestingDavidreynondotcom
from lib.pages.display_work_experience import DisplayWorkExperience


class CriticalPathTests(BaseTestClass):

    def test_refactor_base_url(self):
        home_page = HomePage()
        home_page.go_to_page(self.driver)
        self.assertTrue(home_page.is_on_current_page(self.driver))


    def test_critical_path_click_all_project_tiles_confirm_on_expected_page(self):
        home_page = HomePage()
        home_page.go_to_page(self.driver)
        self.assertTrue(home_page.is_on_current_page(self.driver))
        cards = ComponentProjectCards()
        cards.click_project_card_pytwitservice(self.driver)
        self.assertTrue(DisplayPytwitservice().is_on_current_page(self.driver))
        cards.click_project_card_pop_up_automation(self.driver)
        self.assertTrue(DisplayPopUpAutomation().is_on_current_page(self.driver))
        cards.click_project_card_angular_resume_site(self.driver)
        self.assertTrue(DisplayAngularResumeSite().is_on_current_page(self.driver))
        cards.click_project_card_testing_davidreynondotcom(self.driver)
        self.assertTrue(DisplayTestingDavidreynondotcom().is_on_current_page(self.driver))
        cards.click_project_card_work_experience(self.driver)
        self.assertTrue(DisplayWorkExperience().is_on_current_page(self.driver))

        

    
