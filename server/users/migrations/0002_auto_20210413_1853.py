# Generated by Django 3.1.7 on 2021-04-13 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physioID', models.IntegerField()),
                ('patientID', models.IntegerField()),
                ('testID', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TestDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testName', models.CharField(max_length=100)),
                ('jointName', models.CharField(max_length=100)),
                ('minAngle', models.IntegerField(null=True)),
                ('maxAngle', models.IntegerField(null=True)),
                ('reps', models.IntegerField()),
                ('timePerRep', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientID', models.IntegerField()),
                ('testID', models.IntegerField()),
                ('range', models.DecimalField(decimal_places=2, max_digits=5)),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='physio_id',
        ),
        migrations.AddField(
            model_name='user',
            name='doctorId',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='physioId',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]