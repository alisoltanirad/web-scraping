# https://github.com/alisoltanirad/Web-Scraping.git
# Data Source: https://neuvoo.ca
# Dependencies: BeautifulSoup
import requests
import re
from decimal import Decimal
from bs4 import BeautifulSoup


class Neuvoo:
    start_url = 'https://neuvoo.ca'

    def __init__(self):
        self._page = BeautifulSoup(
            requests.get('https://neuvoo.ca/salary/'), 'html.parser'
        )


def main():
    show_job_salaries(get_job_salaries())


def show_job_salaries(dataset):
    for data in sorted(dataset, key=dataset.get, reverse=True):
        print('{job:>35}: {salary:>8,}'.format(job=data, salary=dataset[data]))


def get_job_salaries():
    salaries = {}
    for job in get_jobs():
        try:
            salaries[get_title(job)] = get_salary(job)
        except:
            continue
    return salaries


def get_title(job):
    return job.find(class_='truncate').text.strip()


def get_salary(job):
    salary = job.find(class_='card--infoList--li--perYear timeBased')
    return Decimal(re.sub(r'[^\d.]', '', salary.text.strip()))


def get_jobs():
    return get_page().find_all(class_='card--infoList--li')


def get_page():
    page = requests.get('https://neuvoo.ca/salary/')
    return BeautifulSoup(page.content, 'html.parser')


if __name__ == '__main__':
    main()