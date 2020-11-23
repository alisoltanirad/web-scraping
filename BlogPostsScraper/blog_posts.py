# https://github.com/alisoltanirad/Web-Scraping.git
# Data Source: https://dev.to
# Dependencies: BeautifulSoup
import requests
from bs4 import BeautifulSoup

class DevBlog():
    url = 'https://dev.to'

    def __init__(self):
        self._page = BeautifulSoup(
            requests.get('https://dev.to').content, 'html.parser'
        )
        self.posts = self._get_posts()


    def post_titles(self):
        for post in self.posts:
            yield (post['title'])


    def _get_posts(self):
        posts = []
        post_elements = self._page.find_all(
            class_='crayons-story__hidden-navigation-link'
        )
        for post_element in post_elements:
            post = {
                'title': post_element.text,
                'link': post_element.get('href'),
            }
            posts.append(post)
        return posts



def main():
    for title in DevBlog().post_titles():
        print(title)


if __name__ == '__main__':
    main()