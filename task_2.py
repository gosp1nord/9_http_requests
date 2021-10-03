import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def hdrs(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        return headers

    def get_load_link(self, path_to_file):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.hdrs()
        params = {
            'path': path_to_file,
            'overwrite': 'true'
        }
        load_link = requests.get(url=url, headers=headers, params=params)
        return load_link.json()

    def upload(self, path_to_file, file_name):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = self.get_load_link(path_to_file=path_to_file).get('href')
        response = requests.put(url, data=open(file_name, "rb"))
        if response.status_code == 201:
            print(f"Файл {file_name} загружен")
        else:
            print("Ошибка загрузки")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "img_1.jpg"
    file_name = "img_1.jpg"
    token = '00000000000000000000000000'
    uploader = YaUploader(token)
    uploader.upload(path_to_file, file_name)
