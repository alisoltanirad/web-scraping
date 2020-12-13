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
        self.tutorials = self._get_tutorials()

    def _get_tutorials(self):
        tutorials = []
        nav_tutorials = self._page.find(id='nav_tutorials')
        tutorial_elements = nav_tutorials.find_all('a')
        for element in tutorial_elements:
            tutorial = {
                'Title': element.text.strip(),
                'URL': self.start_url + element.get('href')
            }
            tutorials.append(tutorial)
        return tutorials


if __name__ == '__main__':

    w3 = W3Schools()

    for tutorial in w3.tutorials:
        print('\t Title: ', tutorial['Title'])
        print('\t URL: ', tutorial['URL'])
        print()