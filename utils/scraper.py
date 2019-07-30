"""Module for scraping"""
from bs4 import BeautifulSoup


class Scraper:
    """Scraper class"""

    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, "lxml")
        print(f"[Scraper] Retrieved page")

    def find_posts(self):
        """Scrapes posts on a page"""

        posts = self.soup.find_all("div", class_="_401d")
        print(f'Found {len(posts)} posts.')
        ## TODO: scrape individula posts and parse their texts and links

        for post in posts:
            try: 
                text = post.find("div", class_="_6-cp").div.get_text()
                a_tag = post.find('span', class_="_6-cm").find('a')
                link = "https://www.facebook.com" + a_tag['href']  
                print(a_tag, text)
            except:
                print("Error occured. Skipped a result.")
        # for post in posts:
        #     text_wrapper = post.find('div', class_="_6-cp")
        #     # text = text_wrapper.children[0]
        #     print(text_wrapper)
        #     a = post.find('span', class_="_6-cm").find('a')
        #     link = "https://www.facebook.com" + a['href']
        #     # print(f'Text: {text}')
        #     print(f'Link: {link}')
