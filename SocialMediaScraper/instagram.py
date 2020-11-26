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
        self._username = username
        self._url = ''.join([self.start_url, self._username])
        self._page = BeautifulSoup(
            requests.get(self._url).content, 'html.parser'
        )
        self._profile = self._get_profile_data()
        self._edges = self._profile['edge_felix_video_timeline']['edges']
        self.data = {
            'Name': self._profile['full_name'],
            'Username': self._username,
            'Page-URL': self._url,
            'Profile-Picture-URL': self._profile['profile_pic_url_hd'],
            'Biography': self._profile['biography'],
            'Website': self._profile['external_url'],
            'Followers': self._profile['edge_followed_by']['count'],
            'Following': self._profile['edge_follow']['count'],
            'Is-Private': self._profile['is_private'],
            'Is_Verified': self._profile['is_verified'],
            'Is-Business-Account': self._profile['is_business_account'],
            'Page-Category': self._profile['category_enum'],
            'Is-Joined-Recently': self._profile['is_joined_recently'],
        }

    def _get_profile_data(self):
        shared_data = self._page.find(
            'script', text=re.compile('window\._sharedData')
        ).string.partition('=')[-1].strip(' ;')

        return json.loads(shared_data)['entry_data']['ProfilePage'][0]['graphql']['user']



def main():
    user = InstagramUser('coder24.7')
    for key, value in user.data.items():
        print('{key:>25}:  {value}'.format(key=key, value=value))

    print(user._edges)


if __name__ == '__main__':
    main()