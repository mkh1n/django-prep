from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        db_table = 'supplier'
        managed = True
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        db_table = 'manufacturer'
        managed = True
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производитеи'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    article = models.CharField(max_length=50, unique=True, verbose_name='Артикул')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    unit_type = models.CharField(max_length=50, default='шт.', verbose_name='Единица измерения')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик', on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name='Категория товара', on_delete=models.PROTECT)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Действующая скидка')
    stock_quantity = models.IntegerField(verbose_name='Кол-во на складе')
    description = models.TextField(max_length=1024, verbose_name='Описание товара')
    photo = models.CharField(max_length=255, blank=True, null=True, verbose_name='Путь к фотографии')

    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.article} {self.name}"
    
    @property
    def price_after_discount(self):
        return self.price * (1 - self.discount / 100)
    
class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Авторизованный клиент'),
        ('manager', 'Менеджер'),
        ('admin', 'Администратор'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, verbose_name='Роль')

    @property
    def is_admin_user(self):
        return self.role == 'Администратор'

    @property
    def is_manager(self):
        return self.role == 'Менеджер'

    @property
    def is_team(self):
        return self.role in ['Менеджер', 'Администратор']