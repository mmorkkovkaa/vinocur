# Generated by Django 2.1.15 on 2024-01-05 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wineshop', '0005_auto_20240105_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('товар', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wineshop.Товары')),
            ],
        ),
        migrations.RemoveField(
            model_name='заказ',
            name='пользователь',
        ),
        migrations.RemoveField(
            model_name='заказ',
            name='товары',
        ),
        migrations.RemoveField(
            model_name='корзина',
            name='заказ',
        ),
        migrations.RemoveField(
            model_name='корзина',
            name='пользователь',
        ),
        migrations.RemoveField(
            model_name='корзина',
            name='товар',
        ),
        migrations.DeleteModel(
            name='Заказ',
        ),
        migrations.DeleteModel(
            name='Корзина',
        ),
    ]
