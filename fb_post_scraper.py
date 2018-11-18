from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Browser():
    
    driver = webdriver.Chrome()

    def get_webpage(self, url):
        self.driver.get(url)
        assert "Facebook" in self.driver.title

    def login(self, email, pswrd):
        elem = self.driver.find_element_by_name("email")
        elem.send_keys(email)
        elem = self.driver.find_element_by_name("pass")
        elem.send_keys(pswrd)
        elem.send_keys(Keys.RETURN)

    def escape(self):
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_tag_name("body")
        elem.send_keys(Keys.ESCAPE)
        self.driver.implicitly_wait(10)
        elem.send_keys(Keys.ESCAPE)

    def search_keyword(self, search_keyword):
        elem = self.driver.find_element_by_name("q")
        elem.send_keys(search_keyword)
        self.driver.implicitly_wait(5)
        elem.send_keys(Keys.RETURN)

    def filter_by(self, filter_name):
        filter_groups = self.driver.find_element_by_partial_link_text(filter_name)
        filter_groups.click()

    #Select SORT BY -> Most Recent
    def sort_by(self, sort_param):
        sort_by_recent = self.driver.find_element_by_partial_link_text(sort_param)
        sort_by_recent.click()

browser = Browser()