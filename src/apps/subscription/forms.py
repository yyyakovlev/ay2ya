from captcha.fields import ReCaptchaField
from django import forms

from apps.subscription.models import Subscription


class SubscriptionForm(forms.ModelForm):
    """ форма для ввода имейла """
    captcha = ReCaptchaField()

    class Meta:
        model = Subscription
        fields = ("email", "captcha")
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "Ваш email ... "})
        }

        labels = {"email": ""}
