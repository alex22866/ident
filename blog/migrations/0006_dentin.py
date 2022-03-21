# Generated by Django 4.0.1 on 2022-03-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_dentin'),
    ]

    operations = [
        migrations.CreateModel(
            name='DentIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Каталог')),
                ('text', models.TextField(default='', max_length=150, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Фото')),
            ],
        ),
    ]
