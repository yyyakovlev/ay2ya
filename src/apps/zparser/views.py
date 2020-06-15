
import requests
# from bs4 import BeautifulSoup as bs

from django.views.generic import TemplateView


class ZparserView(TemplateView):
    template_name = "zparser.html"

    class ZparseCls:

        def zzzparser(self):
            max_page = 3
            pages = []

            for x in range(1, max_page + 1):
                pages.append(requests.get('https://freelance.habr.com/tasks?page=' + str(x) ) )

            for z in pages:
                html = bs(z.content, 'html.parser')

            for elem in html.select('.task__column_desc'):
                title = elem.select('.task__title > a')
                print(title[0].text)