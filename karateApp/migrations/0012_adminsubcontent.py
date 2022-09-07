# Generated by Django 4.1 on 2022-09-07 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karateApp', '0011_admincontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminsubcontent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subheadname', models.CharField(max_length=25)),
                ('subcontparagraph', models.TextField()),
                ('subcontimg', models.ImageField(null=True, upload_to='gallery/')),
                ('maincontid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karateApp.admincontent')),
            ],
        ),
    ]