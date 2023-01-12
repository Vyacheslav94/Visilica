from bs4 import BeautifulSoup
import requests

main_lst = []
main_url = 'https://parsinger.ru/html/index3_page_1.html'
main_response = requests.get(url=main_url)
main_response.encoding = 'utf-8'
soup = BeautifulSoup(main_response.text, 'lxml')
for i in range(1, len(pagen)+1):
    a = []
    url = f'https://parsinger.ru/html/index3_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('a', class_='name_item')
    for txt in div:
        a.append(txt.text)
    main_lst.append(a)
print(main_lst)