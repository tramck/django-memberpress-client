# Generated by Django 3.2.16 on 2022-12-19 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberpress_client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memberpresseventlog',
            options={'verbose_name_plural': 'memberpress event log'},
        ),
        migrations.AlterField(
            model_name='memberpresseventlog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]