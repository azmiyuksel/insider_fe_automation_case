
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from selenium.webdriver.support import expected_conditions as EC

from base.page_base import PageBase
import allure
from locators.locators import CareerPageLocators
from pages.qa_page import QAPage


class CareerPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the page")
    def get_page_title(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains("Insider Careers"))
        return self.driver.title

    def is_locations_section_displayed(self):
        return self.driver.find_element(*CareerPageLocators.locations_section).is_displayed()

    def is_life_section_displayed(self):
        return self.driver.find_element(*CareerPageLocators.life_section).is_displayed()

    def is_teams_section_displayed(self):
        return self.driver.find_element(*CareerPageLocators.teams_section).is_displayed()

    def open_all_teams(self):
        see_all_teams_btn = self.driver.find_element(*CareerPageLocators.see_all_teams_btn)
        self.driver.execute_script("arguments[0].click();", see_all_teams_btn)

    def open_qa_positions(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(CareerPageLocators.qa_btn))
        qa_btn = self.driver.find_element(*CareerPageLocators.qa_btn)
        self.driver.execute_script("arguments[0].click();", qa_btn)
        return QAPage(self.driver)

