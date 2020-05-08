from django.test import Client
from django.test import TestCase

from apps.blog.views import BlogPostView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("post/<int:pk>/")
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(resp.resolver_match.app_name, '')
        self.assertEqual(resp.resolver_match.url_name, 'post')
        self.assertEqual(resp.resolver_match.view_name, 'post')
        self.assertEqual(
            resp.resolver_match.func.__name__, BlogPostView.as_view().__name__
        )

        self.assertEqual(resp.template_name, ["post.html"])