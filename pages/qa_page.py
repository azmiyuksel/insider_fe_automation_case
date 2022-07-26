from base.page_base import PageBase
import allure
from locators.locators import QAPageLocators
from pages.jobs_page import JobsPage


class QAPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the page")
    def get_page_title(self):
        return self.driver.title

    def open_all_qa_jobs(self):
        qa_btn = self.driver.find_element(*QAPageLocators.see_all_qa_jobs_btn)
        self.driver.execute_script("arguments[0].click();", qa_btn)
        return JobsPage(self.driver)

