# from django.test import Client
# from django.test import TestCase
#
# from apps.subscription.views import SubscriptionView
#
#
# class Test(TestCase):
#     def setUp(self) -> None:
#         self.cli = Client()
#
#     def test_get(self):
#         resp = self.cli.get("subscriptions")
#         self.assertEqual(resp.status_code, 200)
#
#         self.assertEqual(resp.resolver_match.app_name, "")
#         self.assertEqual(resp.resolver_match.url_name, "SubscriptionView")
#         self.assertEqual(resp.resolver_match.view_name, "subscription")
