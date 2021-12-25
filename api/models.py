from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Name',
    )
    article = models.IntegerField(
        verbose_name="Article",
        unique=True,
    )
    price = models.FloatField(
        verbose_name='Price',
    )
    image = models.ImageField(
        verbose_name='Product Image',
        upload_to='images/',
        default=0,
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created',
    )

    def __str__(self):
        return f'Product {self.name} with article {self.article} and price {self.price}'

    class Meta:
        verbose_name = 'Product'


class ProductSize(models.Model):
    product = models.ForeignKey(
        to='Product',
        verbose_name='Product',
        on_delete=models.PROTECT,
    )
    size = models.IntegerField(
        verbose_name='Size',
    )
    amount = models.PositiveIntegerField(
        verbose_name='Amount',
        default=0,
    )

    def __str__(self):
        return f'{self.product} with size {self.size} and amount {self.amount}'

    class Meta:
        verbose_name = 'Product size'
        verbose_name_plural = 'Product sizes'


class Storage(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name='Storage Name',
    )
    location = models.CharField(
        max_length=120,
        verbose_name='Storage Location'
    )

    def __str__(self):
        return f'{self.name} on {self.location}'

    class Meta:
        verbose_name = 'Storage'
        verbose_name_plural = 'Storages'


class Shelf(models.Model):
    storage = models.ForeignKey(
        to='Storage',
        on_delete=models.PROTECT,
        verbose_name='Storage',

    )
    number = models.IntegerField(
        verbose_name='Shelf number'
    )

    def __str__(self):
        return f'Shelf number {self.number} on storage {self.storage}'

    class Meta:
        verbose_name = 'Shelf'
        verbose_name_plural = 'Shelves'


class ProductLocation(models.Model):

    product_size = models.ForeignKey(
        to='ProductSize',
        on_delete=models.PROTECT,
        verbose_name='Product size',
    )

    shelf = models.ForeignKey(
        to='Shelf',
        verbose_name='Shelf',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'Product located on shelf {self.shelf}'

    class Meta:
        verbose_name = 'Product location'
        verbose_name_plural = 'Product locations'

