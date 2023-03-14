# Generated by Django 4.1.7 on 2023-03-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your name please!', max_length=300, verbose_name="Ім'я")),
                ('age', models.IntegerField(verbose_name='Вік')),
                ('phone_number', models.IntegerField(verbose_name='Номер телефону')),
                ('address', models.CharField(blank=True, max_length=300, verbose_name='Адреса')),
                ('place_location', models.URLField(blank=True, help_text='You must add http reference your location from google maps', max_length=700, verbose_name='Місце знаходження')),
            ],
        ),
    ]