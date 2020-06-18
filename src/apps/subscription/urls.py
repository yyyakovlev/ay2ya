from django.urls import path

from apps.subscription.views import SubscriptionView

urlpatterns = [
    path("", SubscriptionView.as_view(), name="subscription"),
]
