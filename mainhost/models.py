from django.db import models


class Texts(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"text/run/{self.id}"

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Тексты"


class Modes(models.Model):
    mode = models.CharField('Режим', max_length=100)

    def __str__(self):
        return self.mode

    class Meta:
        verbose_name = "Режим"
        verbose_name_plural = "Режимы"
