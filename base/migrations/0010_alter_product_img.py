# Generated by Django 4.2.6 on 2023-11-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='lion.jpg', null=True, upload_to='products/'),
        ),
    ]
