# from django.test import Client
# from django.test import TestCase
#
# from apps.index.views import IndexView
#
#
# class Test(TestCase):
#     def setUp(self) -> None:
#         self.cli = Client()
#
#     def test_get(self):
#         # breakpoint()
#         resp = self.cli.get('')
#         self.assertEqual(resp.status_code, 200)
#
#         self.assertEqual(resp.resolver_match.app_name, 'index')
#         self.assertEqual(resp.resolver_match.url_name, 'index')
#         self.assertEqual(resp.resolver_match.view_name, 'index')
#         self.assertEqual(resp.resolver_match.func.__name__, IndexView.as_view().__name__)
#
#         self.assertEqual(resp.template_name, ["index.html"])
