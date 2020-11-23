# https://github.com/alisoltanirad/Web-Scraping.git
# Data Source: https://dev.to
# Dependencies: BeautifulSoup
import requests
import re
from decimal import Decimal
from bs4 import BeautifulSoup


def main():
    pass


def get_posts():
    post_links = {}
    post_list = get_page().find_all(class_='crayons-story__hidden-navigation-link')
    for post in post_list:
        post_links[post.text] = post.get('href')
    return post_links


def get_page():
    page = requests.get('https://dev.to')
    return BeautifulSoup(page.content, 'html.parser')


if __name__ == '__main__':
    main()