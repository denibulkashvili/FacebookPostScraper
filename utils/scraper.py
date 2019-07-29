"""Module for scraping"""
from bs4 import BeautifulSoup


class Scraper:
    """Scraper class"""

    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, "lxml")
        print(f"[Scraper] Soup: {self.soup} - Soup")

    def find_posts(self):
        """Scrapes posts on a page"""

        posts = self.soup.find_all("div", class_="_401d")

        ## TODO: scrape individula posts and parse their texts and links

        post = posts[0]
        text = post.find("div", class_="_6-cp").div
        print(text)
        # for post in posts:
        #     text_wrapper = post.find('div', class_="_6-cp")
        #     # text = text_wrapper.children[0]
        #     print(text_wrapper)
        #     a = post.find('span', class_="_6-cm").find('a')
        #     link = "https://www.facebook.com" + a['href']
        #     # print(f'Text: {text}')
        #     print(f'Link: {link}')
