# Generated by Django 5.1.1 on 2024-09-30 20:33

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0003_category_remove_order_customer_remove_menuitem_menu_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='تعداد')),
                ('address', models.CharField(blank=True, default='', max_length=200, verbose_name='آدرس')),
                ('phone', models.CharField(blank=True, default='', max_length=20, verbose_name='شماره تلفن')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='تاریخ')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='مشتری')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.menuitem', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
                'ordering': ('-date',),
            },
        ),
    ]
