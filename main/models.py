from django.db import models


class Codes(models.Model):
    code = models.CharField(max_length=20, verbose_name='Код', unique=True, null=False)
    city = models.CharField(max_length=30, verbose_name='Город', blank=True, null=True)
    short_name = models.CharField(max_length=100, verbose_name='Короткое имя', blank=True, null=True)
    full_name = models.CharField(max_length=100, verbose_name='Полное имя', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.code = '00' + str(self.code)
        return super(Codes, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Список кодов'
        ordering = ['code']
