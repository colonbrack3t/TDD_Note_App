# Generated by Django 4.1.4 on 2022-12-23 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_list_item_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default='',null=True, on_delete=django.db.models.deletion.CASCADE, to='notes_app.list'),
        ),
    ]