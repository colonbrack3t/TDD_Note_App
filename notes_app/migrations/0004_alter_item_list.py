# Generated by Django 4.1.4 on 2022-12-23 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0003_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='notes_app.list'),
        ),
    ]
