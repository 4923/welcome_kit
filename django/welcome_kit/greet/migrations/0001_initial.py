# Generated by Django 4.0.1 on 2022-03-17 09:41

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
            name='Greet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_k', models.TextField(verbose_name='고도희')),
                ('content_h', models.TextField(verbose_name='홍예은')),
                ('content_s', models.TextField(verbose_name='설희관')),
                ('content_p', models.TextField(verbose_name='박경준')),
                ('content_m', models.TextField(verbose_name='민선아')),
                ('content_j', models.TextField(verbose_name='정지원')),
                ('content_c', models.TextField(verbose_name='정우진')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='아기사자')),
            ],
            options={
                'verbose_name': '롤링페이퍼',
                'verbose_name_plural': '롤링페이퍼',
                'db_table': '롤링페이퍼',
            },
        ),
    ]
