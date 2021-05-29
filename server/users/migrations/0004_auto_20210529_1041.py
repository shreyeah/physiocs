# Generated by Django 3.1.7 on 2021-05-29 10:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20210529_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testhistory',
            name='timestamp',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2021, 5, 29, 10, 41, 32, 608056)),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_doc_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='physio_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_physio_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
