from django.test import Client
from django.test import TestCase

from apps.cv.views import CvView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/view_cv/")
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(resp.resolver_match.app_name, "")
        self.assertEqual(resp.resolver_match.url_name, "cv")
        self.assertEqual(resp.resolver_match.view_name, "cv")
        self.assertEqual(resp.resolver_match.func.__name__, CvView.as_view().__name__)

        self.assertEqual(resp.template_name, ["cv.html", "cv/project_list.html"])
