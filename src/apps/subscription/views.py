from django.views.generic import CreateView

from .models import Subscription
from .forms import SubscriptionForm




class SubscriptionView(CreateView):

    model = Subscription
    form_class = SubscriptionForm
    success_url = "/"


# Create your views here.
