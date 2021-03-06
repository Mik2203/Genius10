# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 12:58
from __future__ import unicode_literals

import app_mik.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=500, verbose_name='Заголовок статьи')),
                ('article_text', models.TextField(verbose_name='Описание статьи')),
                ('article_date', models.DateTimeField(auto_now=True, verbose_name='Дата публикиции')),
                ('article_likes', models.IntegerField(default=0)),
                ('article_image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=app_mik.models.upload_location, verbose_name='Изображение', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_date', models.DateTimeField(auto_now=True, verbose_name='datetime')),
                ('comments_text', models.TextField(verbose_name='Комментарий')),
                ('comments_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_mik.Article')),
                ('comments_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
