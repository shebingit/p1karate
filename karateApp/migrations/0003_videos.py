# Generated by Django 4.0.4 on 2022-08-02 06:19

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('karateApp', '0002_alter_associate_members_asm_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kata_name', models.CharField(max_length=50)),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]
