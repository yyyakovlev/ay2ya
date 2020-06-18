import requests
from django.views.generic import TemplateView

from bs4 import BeautifulSoup as BS


class ZparserView(TemplateView):
    template_name = "zparser.html"

    class HabrParser:

        def habr_parser(*args, **kwargs):

            max_page = 3
            pages = []
            n = 0

            for x in range(1, max_page + 1):
                pages.append(requests.get("https://freelance.habr.com/tasks?page=" + str(x)))

            for z in pages:
                html = BS(z.content, "html.parser")

            for elem in html.select(".task__column_desc"):
                title = elem.select(".task__title")
                n += 1
                print(str(n) + '. ' + title[0].text)

