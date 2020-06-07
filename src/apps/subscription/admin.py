from django.contrib import admin

from apps.subscription.models import Subscription

from django.contrib.admin import ModelAdmin


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("email", "date")
