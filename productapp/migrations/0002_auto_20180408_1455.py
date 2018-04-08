# Generated by Django 2.0.3 on 2018-04-08 09:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='Institution',
            field=models.ForeignKey(on_delete=True, related_name='products', to='basic_app.IntitutionModel'),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='categoryid',
            field=models.ForeignKey(on_delete=True, related_name='products', to='productapp.ProductCategoryModel'),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='user',
            field=models.ForeignKey(on_delete=True, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]
