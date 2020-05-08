from django.test import Client
from django.test import TestCase

from apps.blog.views import BlogView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get(' ')
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(resp.resolver_match.app_name, 'blog')
        self.assertEqual(resp.resolver_match.url_name, 'all_post')
        self.assertEqual(resp.resolver_match.view_name, 'all_post')
        self.assertEqual(
            resp.resolver_match.func.__name__, BlogView.as_view().__name__
        )

        self.assertEqual(resp.template_name, ["blog.html"])