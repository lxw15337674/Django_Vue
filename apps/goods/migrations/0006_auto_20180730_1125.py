# Generated by Django 2.0.7 on 2018-07-30 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20180726_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品信息', 'verbose_name_plural': '商品信息'},
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=100, verbose_name='商品名'),
        ),
    ]
