from lib.base_page import BasePage


class ComponentDisplayContainer(BasePage):

    PROPERTIES_FILE = "component_display_container.properties"


    def get_display_container_project_name(self, driver):
        return self.get_element(driver, 'display-container-project-name')

    def get_display_container_content_image(self, driver):
        return self.get_element(driver, 'display-container-content-image')

    def get_display_container_content_long_description(self, driver):
        return self.get_element(driver, 'display-container-content-content-long-description')

    def get_display_container_content_long_description2(self, driver):
        return self.get_element(driver, 'display-container-content-content-long-description2')

    def get_display_container_content_long_description3(self, driver):
        return self.get_element(driver, 'display-container-content-content-long-description3')

    def get_display_container_content_long_description4(self, driver):
        return self.get_element(driver, 'display-container-content-content-long-description4')

    def get_display_container_content_project_url(self, driver):
        return self.get_element(driver, 'display-content-project-url-container')

    def get_display_container_content_project_keywords(self, driver):
        return self.get_element(driver, 'display-content-project-keywords')