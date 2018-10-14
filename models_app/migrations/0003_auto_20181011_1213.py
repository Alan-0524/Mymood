# Generated by Django 2.1.1 on 2018-10-11 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0002_tblhappiness_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblteam',
            name='id',
            field=models.CharField(default=django.utils.timezone.now, max_length=32, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbluser',
            name='id',
            field=models.CharField(default=django.utils.timezone.now, max_length=32, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tblhappiness',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tblhappiness',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tblhappiness',
            name='team_id',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='tblhappiness',
            name='user_id',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='tblreminder',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tblreminder',
            name='user_id',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='tblteam',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tblteam',
            name='team_id',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='tbluser',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tbluser',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tbluser',
            name='team_id',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='tbluser',
            name='user_id',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
