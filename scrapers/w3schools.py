# Data Source: https://w3schools.com
# Dependencies: BeautifulSoup
import requests
from bs4 import BeautifulSoup


class W3Schools:
    start_url = 'https://w3schools.com'

    def __init__(self):
        self._page = BeautifulSoup(
            requests.get(self.start_url).content, 'html.parser'
        )
        self.tutorials = self._get_nav_links('tutorials')
        self.exercises = self._get_nav_links('exercises')

    def _get_nav_links(self, category):
        links = []
        titles = []
        nav = self._page.find(id=('nav_' + category))
        elements = nav.find_all('a')
        for element in elements:
            title = element.get('title')
            if title and (title not in titles):
                link = {
                    'Title': title,
                    'URL': self.start_url + element.get('href')
                }
                links.append(link)
            titles.append(title)
        return links


if __name__ == '__main__':
    w3 = W3Schools()
    for tutorial in w3.tutorials:
        print('\t Title: ', tutorial['Title'])
        print('\t URL: ', tutorial['URL'])
        print()
