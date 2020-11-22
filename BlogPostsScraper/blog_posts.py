# https://github.com/alisoltanirad/Web-Scraping.git
# Data Source: https://dev.to
# Dependencies: BeautifulSoup
import requests
import re
from decimal import Decimal
from bs4 import BeautifulSoup


def main():
    pass


def get_page():
    page = requests.get('https://dev.to/t/react')
    return BeautifulSoup(page.content, 'html.parser')


if __name__ == '__main__':
    main()