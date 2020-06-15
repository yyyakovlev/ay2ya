import requests
from bs4 import BeautifulSoup as BS

max_page = 3
pages = [ ]

for x in range(1, max_page + 1):
    pages.append(requests.get('https://freelance.habr.com/tasks?page=' + str(x) ) )

for z in pages:
    html = BS(z.content, 'html.parser')

for elem in html.select('.task__column_desc'):
    title = elem.select('.task__title > a')
    print(title[0].text)
