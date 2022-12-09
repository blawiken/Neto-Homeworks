import requests
import json
from bs4 import BeautifulSoup
from fake_headers import Headers


SEARCH_TEXT = 'Python'
SEARCH_TEXT = SEARCH_TEXT.replace(' ', '+')
KEYWORDS = [
    'Django',
    'Flask'
]
URLS = [
    f'https://spb.hh.ru/search/vacancy?text={SEARCH_TEXT}&area=1&area=2',
    f'https://hh.ru/search/vacancy?text={SEARCH_TEXT}&area=1&area=2'
]

headers = Headers(
    os='win',
    browser='chrome'
)


def get_page(URL):
    return requests.get(
        URL,
        headers=headers.generate()
    )


def parser_job(job_id):
    title = job_id.find('h3').find('span').text
    url = job_id.find('h3').find('a')['href']
    try:
        wage = job_id.find('span', 'bloko-header-section-3').text
    except:
        wage = 'Не указана'
    try:
        description = job_id.find('div', 'g-user-content').text
    except:
        description = None
    company_name = job_id.find('div', 'vacancy-serp-item__meta-info-company').text
    try:
        city = job_id.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
    except:
        city = None
    city = city.split(' ')
    city = city[0].replace(',', '')

    return {
        'title': title,
        'url': url,
        'description': description,
        'wage': wage,
        'company_name': company_name,
        'city': city
    }


def write_json(dict):
    with open('jobs.json', 'w', encoding='utf8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)


def main():
    all_jobs = {}
    print('Вакансии:')
    for url in URLS:
        page = get_page(url)
        soup = BeautifulSoup(page.text, features='lxml')
        jobs = soup.find_all('div', 'serp-item')

        for job in jobs:
            item = parser_job(job)

            for key_word in KEYWORDS:
                if item['description'] is not None and \
                key_word.lower() in item['description'].lower():

                    all_jobs.update(
                        {
                            item['title']: {
                                'url': item['url'],
                                'wage': item['wage'],
                                'company_name': item['company_name'],
                                'city': item['city']
                            }
                        }
                    )
    write_json(all_jobs)


if __name__ == '__main__':
    main()