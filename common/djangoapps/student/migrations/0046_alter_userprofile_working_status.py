# Generated by Django 3.2.11 on 2022-01-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0045_alter_userprofile_working_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='working_status',
            field=models.CharField(blank=True, choices=[('1', 'I am work'), ('2', 'I dont work')], default=0, max_length=2, null=True),
        ),
    ]