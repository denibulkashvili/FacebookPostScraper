from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Crome driver options
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# disable notifications popup alert
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})


class Browser:
    """Browser class"""

    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=option)

    def get_url(self):
        """Navigates to Facebook mainpage"""
        url = "https://www.facebook.com"
        self.driver.get(url)
        assert "Facebook" in self.driver.title
        print("Visiting Facebook Homepage")

    def login(self, email, pswrd):
        """Logs in usin provided login credentials"""
        elem = self.driver.find_element_by_name("email")
        elem.send_keys(email)
        elem = self.driver.find_element_by_name("pass")
        elem.send_keys(pswrd)
        elem.send_keys(Keys.RETURN)
        print("Login successful.")

    def search_by(self, search_keyword):
        """Initiate the search with keyword"""
        elem = self.driver.find_element_by_name("q")
        elem.send_keys(search_keyword)
        self.driver.implicitly_wait(10)
        elem.send_keys(Keys.RETURN)
        print(f'Searching by keyword {search_keyword}')

    def filter_by(self, filter_name):
        """Apply filters"""
        filter_groups = self.driver.find_element_by_partial_link_text(filter_name)
        filter_groups.click()
        print("Filter applied")

    def sort_by(self, sort_param):
        """Apply sorting parameters"""
        sort_by_recent = self.driver.find_element_by_partial_link_text(sort_param)
        sort_by_recent.click()
        print("Sorted.")
