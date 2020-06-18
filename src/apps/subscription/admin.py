from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.subscription.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("email", "date")
