from django.db import models


class Lugat(models.Model):
    inglizcha = models.CharField('Inglizcha', max_length=128)
    uzbekcha = models.CharField('O`zbekcha', max_length=128)

    class Meta:
        verbose_name = 'Yangiliklar'
        verbose_name_plural = 'Lug`at '
