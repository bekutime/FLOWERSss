from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='flowers.photo', blank=True )
    price = models.DecimalField(max_digits=8,decimal_places=1, default=None)
    description = models.TextField(default=None)
    red = 'Red'
    black = 'Black'
    color = [(red, 'Red'),
             (black, 'Black')
             ]
    color = MultiSelectField(choices=color, default=None, null=True)
    sum = models.PositiveSmallIntegerField(default=0)
    height = models.ForeignKey('Height', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Sort(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Сорт'
        verbose_name_plural = 'Сорты'

    def __str__(self):
        return self.name


class Height(models.Model):
    A = '10'
    B = '20'
    C = '30'
    D = '40'
    E = '50'
    F = '60'

    height = [
        (A, '10'),
        (B, '20'),
        (C, '30'),
        (D, '40'),
        (E, '50'),
        (F, '60')
    ]
    height = models.CharField(max_length=3,choices=height)
    name = models.CharField(max_length=100)
    sort = models.ForeignKey('Sort', models.PROTECT)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class ObjectImage(models.Model):
    """Фото объекта"""
    image = models.ImageField(upload_to='Photo', verbose_name='Фото')
    image_link = models.ForeignKey('Product', verbose_name='Ссылка на объект', on_delete=models.CASCADE,
                                   related_name='image')

    class Meta:
        verbose_name = 'Фото объекта'
        verbose_name_plural = 'Фото объекта'

    def __str__(self):
        return self.image


class Comment(models.Model):
    '''Коменнтарие продукта'''

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()

class Like(models.Model):
    '''Лайки продукта'''

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
