from django.db import models as m


class Subscription(m.Model):
    """ Модель подписки на рассылку """

    email = m.EmailField()
    date = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
