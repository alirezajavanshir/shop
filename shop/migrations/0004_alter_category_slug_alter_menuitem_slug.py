# Generated by Django 5.1.1 on 2024-09-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_remove_order_customer_remove_menuitem_menu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]
