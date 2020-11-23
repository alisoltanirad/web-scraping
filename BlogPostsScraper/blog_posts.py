# https://github.com/alisoltanirad/Web-Scraping.git
# Data Source: https://dev.to
# Dependencies: BeautifulSoup
import requests
import re
from decimal import Decimal
from bs4 import BeautifulSoup


def main():
    show_post_titles()


def show_post_titles():
    posts = get_posts()
    for post in posts:
        print(post['title'])


def get_posts():
    posts = []
    post_elements = get_page().find_all(
        class_='crayons-story__hidden-navigation-link'
    )
    for post_element in post_elements:
        post = {
            'title': post_element.text,
            'link': post_element.get('href'),
        }
        posts.append(post)
    return posts


def get_page():
    page = requests.get('https://dev.to')
    return BeautifulSoup(page.content, 'html.parser')


if __name__ == '__main__':
    main()