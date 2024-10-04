from django.db import models
from django.contrib.auth import get_user_model
from shop.models import MenuItem
import datetime

User = get_user_model()


class Order(models.Model):
    product = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, verbose_name="محصول"
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="مشتری")
    quantity = models.IntegerField(default=1, verbose_name="تعداد")
    address = models.CharField(
        max_length=200, default="", blank=True, verbose_name="آدرس"
    )
    phone = models.CharField(
        max_length=20, default="", blank=True, verbose_name="شماره تلفن"
    )
    date = models.DateField(default=datetime.date.today, verbose_name="تاریخ")
    status = models.BooleanField(default=False, verbose_name="وضعیت")
    discount_code = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="کد تخفیف"
    )

    class Meta:
        ordering = ("-date",)
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"


class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="کد تخفیف")
    discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="درصد تخفیف"
    )
    expiration_date = models.DateField(verbose_name=" تاربخ انقضا")
    products = models.ManyToManyField(MenuItem, verbose_name="لیست محصولات")

    def __str__(self):
        return self.code

    def __str__(self):
        return f"سفارش {self.product.name} برای {self.customer.username}"
