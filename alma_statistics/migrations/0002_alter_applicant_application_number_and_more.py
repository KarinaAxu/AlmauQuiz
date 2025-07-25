# Generated by Django 5.2.3 on 2025-06-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alma_statistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='application_number',
            field=models.CharField(editable=False, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone_number',
            field=models.CharField(help_text='Пример: +77771234567', max_length=20),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='school',
            field=models.CharField(choices=[('Школа Цифровых Технологий', 'Школа Цифровых Технологий'), ('Школа Предпринимательства и инноваций', 'Школа Предпринимательства и инноваций'), ('Школа Менеджмента', 'Школа Менеджмента'), ('Школа Экономики и Финансов', 'Школа Экономики и Финансов'), ('Школа Политики и Права', 'Школа Политики и Права'), ('Школа Медиа и Кино', 'Школа Медиа и Кино')], max_length=150),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='source',
            field=models.CharField(choices=[('Instagram', 'Instagram'), ('Website', 'Website'), ('Facebook', 'Facebook'), ('Threads', 'Threads')], max_length=50),
        ),
    ]
