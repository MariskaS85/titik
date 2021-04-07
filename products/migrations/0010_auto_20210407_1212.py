# Generated by Django 3.1.6 on 2021-04-07 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210330_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='description',
        ),
        migrations.RemoveField(
            model_name='size',
            name='sku',
        ),
        migrations.AddField(
            model_name='size',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.size'),
        ),
        migrations.AlterField(
            model_name='size',
            name='dimension',
            field=models.TextField(),
        ),
    ]