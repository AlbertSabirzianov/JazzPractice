# Generated by Django 4.1.5 on 2023-10-10 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalMap',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(blank=True, verbose_name='О себе')),
                ('stady_level', models.PositiveSmallIntegerField(choices=[(0, 'Не выбранно'), (1, 'Нет музыкального образования'), (2, 'Музыкальная школа'), (3, 'Среднее музыкальное образование'), (4, 'Бакалавриат'), (5, 'Магистратура'), (6, 'Аспирантура')], default=0, verbose_name='Уровень образования')),
                ('stady_course', models.PositiveSmallIntegerField(choices=[(0, 'Не выбранно'), (1, '1й'), (2, '2й'), (3, '3й'), (4, '4й'), (5, '5й')], default=0, verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Персональная карта',
                'verbose_name_plural': 'Персональные карты',
            },
        ),
        migrations.CreateModel(
            name='StudentMap',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('reiting', models.PositiveSmallIntegerField(default=0, verbose_name='Рейтинг')),
                ('start_study', models.DateTimeField(auto_now=True, verbose_name='Начало обучения')),
                ('activiti', models.PositiveSmallIntegerField(default=0, verbose_name='Активность практики')),
            ],
            options={
                'verbose_name': 'Карта студента',
                'verbose_name_plural': 'Карты студентов',
                'ordering': ['-reiting'],
            },
        ),
        migrations.CreateModel(
            name='Feetback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(verbose_name='')),
                ('stars', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Оценка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-pub_time'],
            },
        ),
    ]
