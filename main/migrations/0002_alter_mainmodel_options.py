# Generated by Django 4.0.4 on 2022-07-09 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainmodel',
            options={'ordering': ['-date'], 'verbose_name': 'Main ', 'verbose_name_plural': 'Mains'},
        ),
    ]
