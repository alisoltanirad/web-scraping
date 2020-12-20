# Data Source: https://github.com/
# Dependencies: BeautifulSoup
import re
import requests
from bs4 import BeautifulSoup


class GithubUser:
    start_url = 'https://github.com/'

    def __init__(self, username):
        self.username = username
        self.url = ''.join([self.start_url, self.username])
        self._page = BeautifulSoup(
            requests.get(self.url).content, 'html.parser'
        )

    def get_profile_info(self):
        info = {
            'Username': self.username,
            'Name': self._page.find(
                'span', itemprop='name'
            ).text,
            'Bio': self._page.find(
                'div', class_='user-profile-bio'
            ).text,
            'Followers': self._page.find(
                'a', href='/alisoltanirad?tab=followers'
            ).find('span').text,
            'Following': self._page.find(
                'a', href='/alisoltanirad?tab=following'
            ).find('span').text,
        }
        return info

    def get_activity_info(self):
        timeline_items = [
            re.sub(r'\s+|\n', ' ', item.find('summary').text.strip())
            for item in self._page.find_all(
                'div', class_='TimelineItem-body'
            )
        ]
        print(len(timeline_items))
        info = {
            'Last-Year': re.sub(
                r'\s+|\n',
                ' ',
                self._page.find(
                    'div', class_='js-yearly-contributions'
                ).find('h2').text.strip()
            ),
            'Last-Month': ', '.join(timeline_items)
        }
        return info


if __name__ == '__main__':
    user = GithubUser('alisoltanirad')

    print('\nProfile:\n')
    for key, value in user.get_profile_info().items():
        print('{key}: {value}'.format(key=key, value=value))

    print('\nActivity:\n')
    for key, value in user.get_activity_info().items():
        print('{key}: {value}'.format(key=key, value=value))
