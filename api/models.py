from django.db import models


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

    def __str__(self):
        return f'Product {self.product} with size {self.size}'

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
        return f'Storage {self.name} on {self.location}'

    class Meta:
        verbose_name = 'Storage'
        verbose_name_plural = 'Storages'


class Shelf(models.Model):
    storage = models.ForeignKey(
        to='Storage',
        on_delete=models.PROTECT,
        verbose_name='Storage',
        default=1

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
    product = models.ForeignKey(
        to='Product',
        verbose_name='Product',
        on_delete=models.PROTECT,
    )
    product_size = models.ForeignKey(
        to='ProductSize',
        on_delete=models.PROTECT,
        verbose_name='Product size',
    )
    storage = models.ForeignKey(
        to='Storage',
        verbose_name='Storage',
        on_delete=models.PROTECT,
    )

    shelf = models.ForeignKey(
        to='Shelf',
        verbose_name='Shelf',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'Product {self.product} located on {self.storage} on shelf {self.shelf}'

    class Meta:
        verbose_name = 'Product location'
        verbose_name_plural = 'Product locations'

