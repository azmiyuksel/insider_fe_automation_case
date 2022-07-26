from selenium.webdriver.common.by import By


class HomePageLocators:
    more_btn = (By.XPATH, "//span[text()='More']")
    careers_btn = (By.XPATH, "//h5[text()='Careers']")
    accept_all_cookies_btn = (By.ID, "wt-cli-accept-all-btn")


class CareerPageLocators:
    locations_section = (By.ID, "career-our-location")
    life_section = (By.XPATH, "//section[4]")
    teams_section = (By.ID, "career-find-our-calling")
    see_all_teams_btn = (By.LINK_TEXT, "See all teams")
    qa_btn = (By.XPATH, "//h3[contains(text(),'Quality')]")


class QAPageLocators:
    see_all_qa_jobs_btn = (By.LINK_TEXT, "See all QA jobs")


class JobsPageLocators:
    filter_btn = (By.XPATH, "//span[text()='Filter']")
    filter_by_loc_btn = (By.ID, "select2-filter-by-location-container")
    filter_by_dept_btn = (By.ID, "select2-filter-by-department-container")
    loc_results_section = (By.ID, "select2-filter-by-location-results")
    dept_results_section = (By.ID, "select2-filter-by-department-results")
    jobs_list_section = (By.ID, "jobs-list")
    current_count = (By.XPATH, "//span[@class='totalResult']")
    all_positions = (By.XPATH, "//p[contains(@class, 'position-title')]")
    apply_btn_container = (By.XPATH, "(//div[contains(@class, 'position-list-item')])[1]")
    first_apply_now_btn = (By.XPATH, "(//a[text() = 'Apply Now'])[1]")

    @staticmethod
    def filter_option_by_text(option_text):
        return By.XPATH, f"//li[text()='{option_text}']"

    @staticmethod
    def get_position_by_index(index):
        return By.XPATH, f"(//p[contains(@class, 'position-title')])[{index}]"
