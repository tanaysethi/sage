# Generated by Django 2.2.7 on 2019-11-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_sage_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='trigger_value',
        ),
        migrations.AddField(
            model_name='job',
            name='trigger_args',
            field=models.CharField(default="contrab='0 0 * * *'", max_length=200),
            preserve_default=False,
        ),
    ]