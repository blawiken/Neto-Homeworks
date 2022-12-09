import requests


class YaDisk:
    def __init__(self, ya_token):
        self.ya_token = ya_token

    def create_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.ya_token
        }
        params = {
            'path': folder_name,
            'overwrite': 'true'
        }
        query = requests.put(url, headers=headers, params=params)

        return query.status_code

    def get_files_list(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.ya_token
        }
        params = {
            'path': '/',
            'overwrite': 'true'
        }
        query = requests.get(url, headers=headers, params=params)

        return query.json()

    def delete_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.ya_token
        }
        params = {
            'path': folder_name,
            'overwrite': 'true'
        }
        query = requests.delete(url, headers=headers, params=params)

        return query.status_code
