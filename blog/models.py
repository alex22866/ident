from django.db import models


class Products(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'    #изменить текст
        ordering = ['-created_at']      #дата

    title = models.CharField(max_length=255, verbose_name='Title', default='')
    description = models.TextField(verbose_name='Description', default='')
    image = models.ImageField(upload_to='products', verbose_name='Main image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class DentIn(models.Model):
    title = models.CharField(max_length=255, verbose_name='Каталог',default='')
    text = models.TextField(max_length=150, verbose_name='Текст', default='')
    image = models.ImageField(verbose_name='Фото', null=True, blank=True,default='')

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class New(models.Model):
    datetime = models.DateTimeField(default="")
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(max_length=255, verbose_name='Текст')
    image = models.ImageField(verbose_name='Фото', upload_to='service')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(max_length=250, verbose_name='Текст')
    image = models.ImageField()

    def __str__(self):
        return self.title


