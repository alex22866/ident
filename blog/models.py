from django.db import models

class Products(models.Model):
    pass

class Slider(models.Model):
    title = models.Charfild(max_length=255, verbose_name='Название')
    imege = models.ImegeField(verbose_name='Фото')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

