# Generated by Django 4.1 on 2022-09-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karateApp', '0013_admincontent_contentstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graduations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=30)),
                ('master', models.CharField(max_length=100)),
                ('kyuyear', models.CharField(max_length=130)),
            ],
        ),
    ]
