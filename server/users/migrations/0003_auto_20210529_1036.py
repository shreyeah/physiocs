# Generated by Django 3.1.7 on 2021-05-29 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210529_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testdetails',
            old_name='jointname',
            new_name='joint_name',
        ),
        migrations.RenameField(
            model_name='testdetails',
            old_name='maxangle',
            new_name='max_angle',
        ),
        migrations.RenameField(
            model_name='testdetails',
            old_name='minangle',
            new_name='min_angle',
        ),
        migrations.RenameField(
            model_name='testdetails',
            old_name='testdescription',
            new_name='test_description',
        ),
        migrations.RenameField(
            model_name='testdetails',
            old_name='testname',
            new_name='test_name',
        ),
        migrations.RenameField(
            model_name='testdetails',
            old_name='timeperrep',
            new_name='time_per_rep',
        ),
        migrations.RenameField(
            model_name='testhistory',
            old_name='feedbackstate',
            new_name='feedback_state',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='phno',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='testhistory',
            name='timestamp',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2021, 5, 29, 10, 36, 10, 513088)),
        ),
    ]
