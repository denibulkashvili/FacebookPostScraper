"""FacebookScraper Quickstart"""
from utils import browser, scraper
from dotenv import load_dotenv
import os

# secret info
load_dotenv()
email = os.getenv("FB_EMAIL")
password = os.getenv("FB_PASSWORD")


# Search Settings
keyword = "part-time"
filter_name = "Your Groups"
sort_parameter = "Most Recent"

# Browser Actions
b = browser.Browser()
b.get_url()
b.login(email, password)
b.search_by(keyword)
b.filter_by(filter_name)
b.sort_by(sort_parameter)

# Scraper Actions
s = scraper.Scraper(html=b.driver.page_source)
s.find_posts()
