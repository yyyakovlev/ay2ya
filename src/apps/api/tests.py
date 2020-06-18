from django.test import Client
from django.test import TestCase


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/api/todo/")
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(resp.resolver_match.app_name, "")
        self.assertEqual(resp.resolver_match.url_name, "todo-list")
        self.assertEqual(resp.resolver_match.view_name, "todo-list")
