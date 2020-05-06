from django.test import Client
from django.test import TestCase

from apps.blog.views import BlogView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/view_blg/ ")
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(resp.resolver_match.app_name, "blog")
        self.assertEqual(resp.resolver_match.url_name, "blog")
        self.assertEqual(resp.resolver_match.view_name, "blog")
        self.assertEqual(
            resp.resolver_match.func.__name__, BlogView.as_view().__name__
        )

        self.assertEqual(resp.template_name, ["blog.html"])