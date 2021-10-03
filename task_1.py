import requests


def rqst_intell(name, token):
    url = f'https://superheroapi.com/api/{token}/search/{name}'
    data = requests.get(url)
    if data.status_code != 200:
        print(data.status_code)
        return False
    item = data.json()
    intelligence = item['results'][0]['powerstats']['intelligence']
    return intelligence


if __name__ == '__main__':
    list_name = ['Hulk', 'Captain America', 'Thanos']
    list_intell = []
    for item in list_name:
        intelligence = rqst_intell(item, '2619421814940190')
        if intelligence:
            list_intell.append([item, intelligence])
        else:
            print(f"Неудачный запрос у {item}")
    list_intell.sort(key=lambda x: x[1])
    print(f'Самый умный супергерой - {list_intell[0][0]}, показатель умственных способностей - {list_intell[0][1]}')
