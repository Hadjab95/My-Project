# Generated by Django 5.0.2 on 2024-03-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_product_is_sale_product_sale_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(blank=True, default="", max_length=200, null=True),
        ),
    ]