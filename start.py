from fb_post_scraper import browser, scraper
import login_info as login

# User Settings
email = login.email
pswrd = login.pswrd

# Website Settings
url = "https://www.facebook.com"
keyword = "cover"
filter_name = 'Your Groups'
sort_parameter_name = 'Most Recent'

# Browser Actions
browser.get_webpage(url)
browser.login(email, pswrd)
browser.escape()
browser.search_by(keyword)
browser.filter_by(filter_name)
browser.sort_by(sort_parameter_name)

# Scraper Actions
scraper.find_posts(url)