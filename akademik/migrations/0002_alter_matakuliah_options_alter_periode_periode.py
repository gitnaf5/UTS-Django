# Generated by Django 5.1.3 on 2024-12-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matakuliah',
            options={'verbose_name': 'mata kuliah', 'verbose_name_plural': 'mata kuliah'},
        ),
        migrations.AlterField(
            model_name='periode',
            name='periode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]