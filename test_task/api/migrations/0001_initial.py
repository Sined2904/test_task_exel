# Generated by Django 4.2.9 on 2024-01-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('file', models.FileField(help_text='Загрузите файл на проверку', upload_to='docs/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'ordering': ('-pub_date',),
            },
        ),
    ]