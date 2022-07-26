import logging
import time

from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.page_base import PageBase
import allure

from locators.locators import JobsPageLocators


class JobsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the page")
    def get_page_title(self):
        return self.driver.title

    @allure.step("Getting page URL")
    def get_page_url(self):
        return self.driver.current_url

    @allure.step("Filtering")
    def filter_jobs(self, location, department):
        time.sleep(3)
        ignored_exceptions = (StaleElementReferenceException, NoSuchElementException, )
        filter_by_loc_btn = WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(EC.element_to_be_clickable(JobsPageLocators.filter_by_loc_btn))
        filter_by_loc_btn.click()
        filter_by_loc_item = WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions)\
            .until(EC.element_to_be_clickable(JobsPageLocators.filter_option_by_text(location)))
        try:
            filter_by_loc_item.click()
        except StaleElementReferenceException as e:
            logging.exception(f"StaleElementReferenceException is raised: {e.msg}")

        filter_by_dept_btn = WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(EC.element_to_be_clickable(JobsPageLocators.filter_by_dept_btn))
        filter_by_dept_btn.click()
        filter_by_dept_btn = WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(EC.element_to_be_clickable(JobsPageLocators.filter_option_by_text(department)))
        try:
            filter_by_dept_btn.click()
        except StaleElementReferenceException as e:
            logging.exception(f"StaleElementReferenceException is raised: {e.msg}")

    @allure.step("Getting Current Job Count")
    def get_current_job_count(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(JobsPageLocators.current_count))
        current_count = self.driver.find_element(*JobsPageLocators.current_count).text
        return int(current_count)

    @allure.step("Getting position text")
    def get_position_text_by_index(self, index):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(JobsPageLocators.get_position_by_index(index)))
        return self.driver.find_element(*JobsPageLocators.get_position_by_index(index)).text

    @allure.step("Getting filtered position count")
    def get_position_count_by_name(self, pos_name):
        pos_count = len(self.driver
                           .find_elements(By.XPATH,
                                          f"(//p[contains(@class, 'position-title') "
                                          f"and (contains(text(), '{pos_name}'))])"))
        return pos_count

    @allure.step("Getting filtered department count")
    def get_dept_count_by_name(self, dept_name):
        dept_count = len(self.driver.find_elements(By.XPATH,
                                                   f"//span[contains(@class, 'position-department') "
                                                   f"and text()='{dept_name}']"))
        return dept_count

    @allure.step("Getting filtered location count")
    def get_loc_count_by_name(self, loc_name):
        loc_count = len(self.driver.find_elements(By.XPATH,
                                                  f"//div[contains(@class, 'position-location') "
                                                  f"and text()='{loc_name}']"))
        return loc_count

    @allure.step("Getting Apply Now button count")
    def get_apply_now_btn_count(self):
        apply_now_btn_count = len(self.driver.find_elements(By.XPATH,
                                                            f"//a[contains(@class, 'btn') and text()='Apply Now']"))
        return apply_now_btn_count

    @allure.step("Clicking first Apply Now button")
    def get_href_first_apply_now_btn(self):
        url = self.driver.find_elements(*JobsPageLocators.first_apply_now_btn)[0].get_attribute('href')
        return url
