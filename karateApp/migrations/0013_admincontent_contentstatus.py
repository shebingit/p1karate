# Generated by Django 4.1 on 2022-09-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karateApp', '0012_adminsubcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='admincontent',
            name='contentstatus',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
