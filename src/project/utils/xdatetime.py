from datetime import date
from datetime import datetime
from typing import NamedTuple
from typing import Optional
from typing import Union

import pytz
import requests
from delorean import Delorean
from django.conf import settings
from django.http import HttpRequest
from ipware import get_client_ip

from project.utils.safeguards import safe


def utcnow() -> datetime:
    return Delorean().datetime


def now(timezone: Optional[str] = None) -> datetime:
    tz = timezone or settings.TIME_ZONE
    return Delorean().shift(tz).datetime


def get_user_hour(request: HttpRequest) -> int:
    atm = now()
    hour = atm.hour

    if tz := get_user_tz(request):
        hour = Delorean(atm).shift(str(tz)).datetime.hour

    return hour


def get_user_tz(request: HttpRequest) -> Union[pytz.BaseTzInfo, None]:
    ip = get_client_ip(request)[0]
    if not (tz_name := retrieve_tz(ip)):
        return None
    return pytz.timezone(tz_name)


@safe
def retrieve_tz(ip: str):
    resp = requests.get(f"http://ip-api.com/json/{ip}")
    if resp.status_code != 200:
        return None

    payload = resp.json()
    tz_name = payload.get("timezone")
    return tz_name


class DateDelta(NamedTuple):
    years: int
    months: int

    def __str__(self):
        parts = []

        if self.years:
            suffix = "s" if (self.years % 10) != 1 else ""
            parts.append(f"{self.years} y{suffix}")

        if self.months:
            suffix = "s" if (self.months % 10) != 1 else ""
            parts.append(f"{self.months} mo{suffix}")

        if not any((self.years, self.months)):
            parts.append("<1 mo")

        return " ".join(parts)

    @classmethod
    def build(cls, start: date, finish: Optional[date] = None) -> "DateDelta":
        finish = finish or utcnow().date()
        delta = finish - start
        years, days = divmod(delta.days, 365)
        months = days // 30
        return DateDelta(years=years, months=months)
