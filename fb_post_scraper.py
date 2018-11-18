from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

class Browser():
    
    def get_webpage(self, url):
        driver.get(url)
        assert "Facebook" in driver.title

    def login(self, email, pswrd):
        elem = driver.find_element_by_name("email")
        elem.send_keys(email)
        elem = driver.find_element_by_name("pass")
        elem.send_keys(pswrd)
        elem.send_keys(Keys.RETURN)

    def escape(self):
        driver.implicitly_wait(10)
        elem = driver.find_element_by_tag_name("body")
        elem.send_keys(Keys.ESCAPE)
        driver.implicitly_wait(10)
        elem.send_keys(Keys.ESCAPE)

    def search_keyword(self, search_keyword):
        elem = driver.find_element_by_name("q")
        elem.send_keys(search_keyword)
        driver.implicitly_wait(5)
        elem.send_keys(Keys.RETURN)

    def filter_by(self, filter_name):
        filter_groups = driver.find_element_by_partial_link_text(filter_name)
        filter_groups.click()

    #Select SORT BY -> Most Recent
    def sort_by(self, sort_param):
        sort_by_recent = driver.find_element_by_partial_link_text(sort_param)
        sort_by_recent.click()

browser = Browser()