# Generated by Django 4.0.4 on 2022-05-26 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='awsimage',
            old_name='image',
            new_name='images',
        ),
    ]