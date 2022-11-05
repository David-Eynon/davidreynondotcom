from lib.base_page import BasePage

class ComponentProjectCards(BasePage):

    PROPERTIES_FILE = "component_project_cards.properties"

    """ This can easily be refactored. For now, pass in a label
    and encapsulate this with a specific function mentioning exact
    label in human form.

    Example:
        def get_card_angular_project(self):
            return get_card('angular_property')
    """


    def get_project_card_pytwitservice(self, driver):
        return self.get_element(driver, 'project-card-pytwitservice')

    def get_project_card_pop_up_automation(self, driver):
        return self.get_element(driver, 'project-card-pop-up-automation')        

    def get_project_card_angular_resume_site(self, driver):
        return self.get_element(driver, 'project-card-angular-resume-site')        

    def get_project_card_testing_davidreynondotcom(self, driver):
        return self.get_element(driver, 'project-card-testing-davidreynondotcom')        

    def get_project_card_work_experience(self, driver):
        return self.get_element(driver, 'project-card-work-experience')        


    def click_project_card_pytwitservice(self, driver):
        self.get_project_card_pytwitservice(driver).click()

    def click_project_card_pop_up_automation(self, driver):
        self.get_project_card_pop_up_automation(driver).click()

    def click_project_card_angular_resume_site(self, driver):
        self.get_project_card_angular_resume_site(driver).click()

    def click_project_card_testing_davidreynondotcom(self, driver):
        self.get_project_card_testing_davidreynondotcom(driver).click()

    def click_project_card_work_experience(self, driver):
        self.get_project_card_work_experience(driver).click()
