from django import template
from apps.subscription.forms import SubscriptionForm

register = template.Library()

@register.inclusion_tag("form.html")
def subscription_form():
    return {"subscription_form": SubscriptionForm()}
