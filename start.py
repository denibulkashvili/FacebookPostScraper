"""Scraper Quickstart"""
from utils import browser
from assets.login_info import email, pswrd

# Website Settings
url = "https://www.facebook.com"
keyword = "cover"
filter_name = 'Your Groups'
sort_parameter = 'Most Recent'

# Browser Actions
b = browser.Browser()
b.get_url()
b.login(email, pswrd)
b.search_by(keyword)
b.filter_by(filter_name)
b.sort_by(sort_parameter)

# Scraper Actions
