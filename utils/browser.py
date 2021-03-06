"""Browser Module"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

# Crome driver options
OPTION = Options()

OPTION.add_argument("--disable-infobars")
OPTION.add_argument("start-maximized")
OPTION.add_argument("--disable-extensions")
# disable notifications popup alert
OPTION.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)


class Browser:
    """Browser class"""

    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=OPTION)

    def get_url(self):
        """Navigates to Facebook mainpage"""
        url = "https://www.facebook.com"
        self.driver.get(url)
        assert "Facebook" in self.driver.title
        print("[Browser] Visiting Facebook Homepage")

    def login(self, email, pswrd):
        """Logs in usin provided login credentials"""
        elem = self.driver.find_element_by_name("email")
        elem.send_keys(email)
        elem = self.driver.find_element_by_name("pass")
        elem.send_keys(pswrd)
        elem.send_keys(Keys.RETURN)
        print("[Browser] Login successful.")

    def search_by(self, search_keyword):
        """Initiate the search with keyword"""
        try: 
            elem = self.driver.find_element_by_name("q")
            elem.send_keys(search_keyword)
            # self.driver.implicitly_wait(20)
            elem.send_keys(Keys.RETURN)
            print(f"[Browser] Searching by keyword {search_keyword}")
        except (StaleElementReferenceException):
            print("[Error] Error searching by keyword")

    def filter_by(self, filter_name):
        """Apply filters"""
        self.driver.implicitly_wait(10)
        try:
            filter_groups = self.driver.find_element_by_partial_link_text(filter_name)
            filter_groups.click()
            print("[Browser] Filter applied")
        except (NoSuchElementException) as e:
            print(f"[Error] Couldn't find the selector {filter_name}. - {e}")

    def sort_by(self, sort_param):
        """Apply sorting parameters"""
        try:
            sort_by_recent = self.driver.find_element_by_partial_link_text(sort_param)
            sort_by_recent.click()
            print("[Browser] Sorted.")
        except (NoSuchElementException) as e:
            print(f"[Error] Couldn't find the sorting parameter {sort_param}. - {e}")

    def get_source(self):
        """Returns current page source html"""
        return self.driver.page_source.encode('utf-8')