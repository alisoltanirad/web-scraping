# https://github.com/alisoltanirad/Web-Scraping.git
# Data Source: https://instagram.com
# Dependencies: BeautifulSoup
import requests
import re
import json
from bs4 import BeautifulSoup

class InstagramUser():
    start_url = 'https://instagram.com/'

    def __init__(self, username):
        self.username = username
        self.url = ''.join([self.start_url, self.username])
        self._page = BeautifulSoup(
            requests.get(self.url).content, 'html.parser'
        )
        self._data = self._get_profile_data()

    def _get_profile_data(self):
        shared_data = self._page.find(
            'script', text=re.compile('window\._sharedData')
        ).string.partition('=')[-1].strip(' ;')

        return json.loads(shared_data)



def main():
    coder = InstagramUser('coder24.7')


if __name__ == '__main__':
    main()