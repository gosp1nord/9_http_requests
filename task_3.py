import requests
import csv
import time


def request(page_num):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'fromdate': '1633132800',
        'tagged': 'Python',
        'site': 'stackoverflow',
        'page': page_num
    }
    response = requests.get(url=url, params=params)
    data = response.json()
    return data


def processing_request(data, list_responses):
    for i in range(len(data['items'])):
        question_id = data['items'][i]['question_id']
        title = data['items'][i]['title']
        link = data['items'][i]['link']
        list_responses.append([question_id, title, link])
    has_more = data['has_more']
    return has_more


def writing(list_responses):
    csv.register_dialect("customcsv", delimiter=';')
    with open('result.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, "customcsv")
        writer.writerows(list_responses)


if __name__ == '__main__':
    page_num = 1
    has_more = True
    list_responses = [['question_id', 'title', 'link']]
    while has_more:
        data = request(page_num)
        has_more = processing_request(data, list_responses)
        print(f"Запрос {page_num} выполнен")
        time.sleep(1)
        page_num += 1
    writing(list_responses)
    print("Работа окончена, результаты записаны в файл")
