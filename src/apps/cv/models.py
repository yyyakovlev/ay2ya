from django.db import models as m

class Techno(m.Model):
    name = m.TextField(unique=True)
    description = m.TextField(null=True, blank=True)

    def __str__(self):
        return f"#(id={self.pk}, name={self.name!r})"


class Project(m.Model):
    start = m.DateField(null=True, blank=True)
    end = m.DateField(null=True, blank=True)
    comp = m.TextField(null=True, blank=True)
    summary = m.TextField(null=True, unique=True)
    # python = m.BooleanField() - чек бокс 1 или 0
    # django = m.BooleanField() - чек бокс 1 или 0
    technos = m.ManyToManyField(Techno, related_name="project") #связка двух моделей по projects

class Resposibility(m.Model):
    project = m.ForeignKey(Project, on_delete=m.CASCADE, related_name='responsibilities')
    summary = m.TextField()

    #
    # class Meta:
    #     verbose_name_plural = "User Info"
    #
    # # Отображение текста в админке
    # def __str__(self):
    #     return f"UserInfo(id={self.pk}, name={self.name!r})"
