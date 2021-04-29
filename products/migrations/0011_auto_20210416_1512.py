# Generated by Django 3.1.6 on 2021-04-16 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210407_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.size'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
