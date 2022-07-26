from base.page_base import PageBase
import allure
from locators.locators import HomePageLocators
from pages.career_page import CareerPage


class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the page")
    def get_page_title(self):
        return self.driver.title

    @allure.step("Opening Career page")
    def open_career_page(self):
        more_btn = self.driver.find_element(*HomePageLocators.more_btn)
        self.driver.execute_script("arguments[0].click();", more_btn)
        careers_btn = self.driver.find_element(*HomePageLocators.careers_btn)
        self.driver.execute_script("arguments[0].click();", careers_btn)
        return CareerPage(self.driver)

    @allure.step("Cookies are accepted")
    def accept_all_cookies(self):
        accept_btn = self.driver.find_element(*HomePageLocators.accept_all_cookies_btn)
        accept_btn.click()
