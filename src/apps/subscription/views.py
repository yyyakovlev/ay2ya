from django.views.generic import CreateView

from apps.subscription.forms import SubscriptionForm
from apps.subscription.models import Subscription


class SubscriptionView(CreateView):

    model = Subscription
    form_class = SubscriptionForm
    success_url = "/"


# Create your views here.
