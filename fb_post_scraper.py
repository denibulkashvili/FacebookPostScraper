from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import login_info as login

#Get the webpage
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
assert "Facebook" in driver.title

#Login info
email = login.email
pswrd = login.pswrd

# Login
elem = driver.find_element_by_name("email")
elem.send_keys(email)
elem = driver.find_element_by_name("pass")
elem.send_keys(pswrd)
elem.send_keys(Keys.RETURN)


driver.implicitly_wait(10)
elem = driver.find_element_by_tag_name("body")
elem.send_keys(Keys.ESCAPE)
driver.implicitly_wait(10)
elem.send_keys(Keys.ESCAPE)

# Search for a keyword
search_keyword = "cover"
elem = driver.find_element_by_name("q")
elem.send_keys(search_keyword)
driver.implicitly_wait(5)
elem.send_keys(Keys.RETURN)


# Select POSTS FROM -> Your Groups
filter_groups = driver.find_element_by_partial_link_text('Your Groups')
filter_groups.click()

#Select SORT BY -> Most Recent
sort_by_recent = driver.find_element_by_partial_link_text('Most Recent')
sort_by_recent.click()