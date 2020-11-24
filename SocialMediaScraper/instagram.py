# https://github.com/alisoltanirad/Web-Scraping.git
# Data Source: https://instagram.com
# Dependencies: BeautifulSoup
import requests
from bs4 import BeautifulSoup

class InstagramUser():
    start_url = 'https://instagram.com/'

    def __init__(self, username):
        self.username = username
        self.url = ''.join([self.start_url, self.username])
        self.page = BeautifulSoup(
            requests.get(self.url).content, 'html.parser'
        )


def main():
    coder = InstagramUser('coder24.7')
    print(coder.page)


if __name__ == '__main__':
    main()