# Generated by Django 4.0.4 on 2023-02-22 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_userreqester'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(max_length=600)),
            ],
        ),
    ]
