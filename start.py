"""FacebookScraper Quickstart"""
from utils import browser, scraper
from assets.login_info import email, pswrd

# Search Settings
keyword = "cover"
filter_name = "Your Groups"
sort_parameter = "Most Recent"

# Browser Actions
b = browser.Browser()
b.get_url()
b.login(email, pswrd)
b.search_by(keyword)
b.filter_by(filter_name)
b.sort_by(sort_parameter)

# Scraper Actions
s = scraper.Scraper(html=b.driver.page_source)
s.find_posts()
