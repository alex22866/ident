# Generated by Django 4.0.1 on 2022-03-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=250, verbose_name='Текст')),
                ('image', models.ImageField(height_field=412, upload_to='', verbose_name='Видео', width_field=832)),
            ],
        ),
    ]