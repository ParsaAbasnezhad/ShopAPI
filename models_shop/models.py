import datetime
from django.utils import timezone
from django.db import models


class Category(models.Model):
    """دسته‌بندی محصولات (مثلاً: اسپرسو، عربیکا، دستگاه آسیاب، قطعات و ...)"""
    name = models.CharField(max_length=100, unique=True, verbose_name="نام دسته‌بندی")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to="categories/", blank=True, null=True, verbose_name="تصویر")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ایجاد")

    class Meta:
        ordering = ['name']
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name


class Product(models.Model):
    PRODUCT_TYPES = [
        ('coffee', 'Coffee'),  # قهوه
        ('machine', 'Coffee Machine'),  # دستگاه
        ('part', 'Coffee Part'),  # قطعه
    ]
    CONDITION_TYPES = [
        ('new', 'نو'),
        ('used', 'دست دوم'),
    ]
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")
    stock = models.PositiveIntegerField(default=0, verbose_name="موجودی")
    image = models.ImageField(upload_to="products/", verbose_name="تصویر")
    type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default='coffee', verbose_name="نوع محصول")
    condition = models.CharField(max_length=10, choices=CONDITION_TYPES, default='new', verbose_name="وضعیت")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="دسته‌بندی")
    is_featured = models.BooleanField(default=False, verbose_name="محصول ویژه")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین تغییر")
