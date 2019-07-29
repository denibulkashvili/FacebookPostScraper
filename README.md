# Facebook Post Scraper

## Description

> Note: this script is a work-in-progress project. Some parts of it may not be finished or may be subject to change.

Facebook Post Scraper is a small Python script for searching and scraping posts from a Facebook search. 

## Tools Used

* Selenium
* BeautifulSoup
* (In development) PostgreSQL

## Installation and Use

1. Clone the project. 
    ```
    https://github.com/denibulkashvili/FacebookPostScraper.git
    ```
2. Create new virtual environment, activate it and install required packages
    ```
    pip install -r requirements.txt
    ```
3. Rename `env.sample` into `.env` and update with your login info
4. Update seach keyword and other ssearch settings in `start.py`
5. Run `python start.py` from the terminal