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

    def profile_info(self):
        return {

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

            'URL': self.url,

        }

    def activity_info(self):
        timeline_items = [
            re.sub(r'\s+|\n', ' ', item.find('summary').text.strip())
            for item in self._page.find_all(
                'div', class_='TimelineItem-body'
            )
        ]

        return {
            'Last-Year': re.sub(
                r'\s+|\n',
                ' ',
                self._page.find(
                    'div', class_='js-yearly-contributions'
                ).find('h2').text.strip()
            ),

            'Last-Month': ', '.join(timeline_items)
        }

    def repos_info(self):
        page = self._get_tab('repositories')

        repos = list()
        for repo in page.find_all('li', class_='public'):
            repos.append({

                'Title': repo.find(
                    'a', itemprop='name codeRepository'
                ).text.strip(),

                'Description': repo.find(
                    'p', itemprop='description'
                ).text.strip() if repo.find(
                    'p', itemprop='description'
                ).text.strip() is not None else 'None',

                'Language': repo.find(
                    'span', itemprop='programmingLanguage'
                ).text.strip() if repo.find(
                    'span', itemprop='programmingLanguage'
                ) is not None else 'None',
                
                'Updated': repo.find(
                    'relative-time'
                ).text.strip(),

                'Tags': ', '.join(
                    tag.text.strip() for tag in repo.find_all(
                        'a', class_='topic-tag'
                    )
                ) if repo.find_all('a', class_='topic-tag') != [] else 'None',

                'URL': ''.join([
                    self.start_url,
                    repo.find(
                    'a', itemprop='name codeRepository'
                    ).get('href')[1:]
                ]),

            })

        return repos

    def _get_tab(self, name):
        url = ''.join([self.url, '?tab=', name])
        return BeautifulSoup(
            requests.get(url).content, 'html.parser'
        )


if __name__ == '__main__':
    user = GithubUser('alisoltanirad')

    print('\n\tProfile:\n')
    for key, value in user.profile_info().items():
        print('{key}: {value}'.format(key=key, value=value))

    print('\n\tActivity:\n')
    for key, value in user.activity_info().items():
        print('{key}: {value}'.format(key=key, value=value))

    print('\n\tRepositories:\n')
    for repo in user.repos_info():
        for key, value in repo.items():
            print('{key}: {value}'.format(key=key, value=value))
        print()