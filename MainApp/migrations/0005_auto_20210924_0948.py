# Generated by Django 3.1 on 2021-09-24 09:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0004_auto_20210923_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 24, 9, 48, 4, 757188)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='snippet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='MainApp.snippet'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 24, 9, 48, 4, 756724)),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='lang',
            field=models.CharField(choices=[('c#', 'C#'), ('cpp', 'C++'), ('js', 'JavaScript'), ('php', 'PHP'), ('py', 'Python')], max_length=30),
        ),
    ]
