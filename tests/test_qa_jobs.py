import logging
import time

import pytest
import allure

from locators.locators import JobsPageLocators
from pages.home_page import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestQAJobs:

    @allure.title("Career page - smoke test")
    @allure.description("Check if Apply Now button redirects Lever page")
    def test_qa_jobs(self):
        home_page = HomePage(self.driver)
        home_page.open()
        assert("Insider" in home_page.get_page_title())
        home_page.accept_all_cookies()
        career_page = home_page.open_career_page()
        assert("Insider Careers" in career_page.get_page_title())
        assert career_page.is_locations_section_displayed()
        assert career_page.is_life_section_displayed()
        assert career_page.is_teams_section_displayed()
        career_page.open_all_teams()
        qa_page = career_page.open_qa_positions()
        jobs_page = qa_page.open_all_qa_jobs()
        jobs_page.filter_jobs("Istanbul, Turkey", "Quality Assurance")
        assert jobs_page.driver.find_element(*JobsPageLocators.jobs_list_section).is_displayed
        time.sleep(3)
        current_job_count = jobs_page.get_current_job_count()
        logging.info(f"Current Job Count: {current_job_count}")
        if current_job_count <= 12:
            assert current_job_count == jobs_page.get_position_count_by_name('Quality Assurance') \
                   + jobs_page.get_position_count_by_name('QA')

            assert current_job_count == jobs_page.get_dept_count_by_name('Quality Assurance')
            assert current_job_count == jobs_page.get_loc_count_by_name('Istanbul, Turkey')
            assert current_job_count == jobs_page.get_apply_now_btn_count()
            logging.info(jobs_page.get_href_first_apply_now_btn())
            assert str(jobs_page.get_href_first_apply_now_btn()).__contains__("https://jobs.lever.co/useinsider")
        else:
            # TODO: If current_job_count is bigger than 12, traversing page function should be implemented.
            raise NotImplementedError





