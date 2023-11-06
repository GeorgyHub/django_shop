from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image

# Create your models here.
class Items(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    ItemName = models.CharField(max_length=50, null=True, verbose_name = "Имя товара")
    ItemPhoto = models.ImageField(upload_to='media/image/items', verbose_name = "Изображение товара")
    ItemCategories = models.ForeignKey('Categories', on_delete = models.CASCADE, verbose_name = "Категория")
    ItemPrice = models.IntegerField(null=True, verbose_name = "Цена")
    ItemBacketCount = models.IntegerField(verbose_name = "Кол-во товаров в корзине")
    ItemText = models.TextField(null=True, verbose_name = "Описание")
    Item = models.BooleanField(default=True, verbose_name = "Есть в наличии")
    ItemNameBrand = models.ForeignKey('Brands', on_delete = models.CASCADE, null=True, verbose_name = "Имя брэнда")
    #ItemImageBrand = models.ForeignKey('Brands', on_delete = models.CASCADE, verbose_name = "Лого брэнда")

    def __str__(self):
        return self.ItemName

    def get_absolute_url(self):
        return f"/item/{self.ItemName}"

class Categories(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    ItemCategories = models.CharField(max_length=100, verbose_name = "Категория")

    def __str__(self):
        return self.ItemCategories

class Brands(models.Model):
    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'

    NameBrand = models.CharField(max_length=100, null=True, verbose_name = "Имя брэнда")
    ImageBrand =models.ImageField(upload_to='media/image/logo', verbose_name = "Лого брэнда")

    def __str__(self):
        return self.NameBrand