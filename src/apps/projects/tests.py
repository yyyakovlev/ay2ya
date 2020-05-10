from django.test import Client
from django.test import TestCase

from apps.projects.views import ProjectsView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/view_prj/")
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(resp.resolver_match.app_name, "")
        self.assertEqual(resp.resolver_match.url_name, "all_prj")
        self.assertEqual(resp.resolver_match.view_name, "all_prj")
        self.assertEqual(
            resp.resolver_match.func.__name__, ProjectsView.as_view().__name__
        )

        self.assertEqual(resp.template_name, ["projects.html"])
