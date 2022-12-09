import requests
import os 
import json
from datetime import date


class VK:
    def __init__(self, vk_token):
        self.vk_token = vk_token
    
    def get_photos(self, user_id, count=5):
        url = "https://api.vk.com/method/photos.get"
        params = {
            "owner_id": user_id,
            "album_id": "profile",
            "access_token": self.vk_token,
            "v": "5.131",
            "extended": "1",
            "photo_sizes": "1",
            "count": count
        }
        response = requests.get(url, params)
        return response.json()

    def download(self, user_id):
        photos = self.get_photos(user_id)
        photos_data = photos["response"]["items"]
        print(f"Number of photos to download: {len(photos_data)}")
        photos_info = []

        if not os.path.exists("images"):
                os.mkdir("images")

        for photo in photos_data:
            photo_name = f"{date.today()}_{str(photo['likes']['count'])}.jpg"

            for size in photo["sizes"]:
                photo_size = size["type"]
                photo_url = size["url"]

            photos_info.append({
                "file_name": photo_name,
                "size": photo_size
            })

            with open("images/%s" % photo_name, "wb") as picture:
                image = requests.get(photo_url)
                picture.write(image.content)
                print(f"Picture {photo_name} saved.")

            with open("photos.json", "w") as file:
                json.dump(photos_info, file, indent=4)

        print("Download from VK complete!")
        return photos_info
        

class YaDisk:
    def __init__(self, ya_token):
        self.ya_token = ya_token

    def create_folder(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources/"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.ya_token
        }
        params = {
            "path": "photos_from_vk",
            "overwrite": "true"
        }
        requests.put(url, headers=headers, params=params)

    def upload(self, file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.ya_token
        }
        params = {
            "path": f"photos_from_vk/{file_path}",
            "overwrite": "true"
        }
        response = requests.get(url, headers=headers, params=params)
        upload_link = response.json()["href"]
        requests.put(upload_link, open(f"images/{file_path}", "rb"))
        print(f"File {file_path} upload to YaDisk.")

    def mass_upload(self, photos):
        self.create_folder()
        for photo in photos:
            file_name = photo["file_name"]
            self.upload(file_name)
        print("Upload yo YaDisk complete!")
        print(f"Number of photos to upload: {len(photos)}")


if __name__ == "__main__":
    VK_TOKEN = ""
    user_id = str(input("Enter VK user id: "))
    ya_token = str(input("Enter Yandex token: "))
    
    vk_download = VK(VK_TOKEN)
    photos = vk_download.download(user_id)
    ya_disk = YaDisk(ya_token)
    ya_disk.mass_upload(photos)