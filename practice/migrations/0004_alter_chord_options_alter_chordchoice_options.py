# Generated by Django 4.1.5 on 2023-04-03 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_chord'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chord',
            options={'verbose_name': 'Аккорд', 'verbose_name_plural': 'Аккорды'},
        ),
        migrations.AlterModelOptions(
            name='chordchoice',
            options={'ordering': ['-choice_time'], 'verbose_name': 'Угаданный аккорд', 'verbose_name_plural': 'Угаданные аккорды'},
        ),
    ]