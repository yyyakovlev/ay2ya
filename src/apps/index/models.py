from django.db import models as m


class UserInfo(m.Model):
    name = m.TextField(unique=True)
    grts = m.TextField(null=True, blank=True)
    age = m.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "User Info"

    # Отображение текста в админке
    def __str__(self):
        return f"UserInfo(id={self.pk}, name={self.name!r})"


# a = UserInfo()
#
# print(a.name)


# Create your models here.
