# Generated by Django 4.1.4 on 2022-12-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_donor_allergies_alter_donor_bleeding_disorders_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='blood_group',
            field=models.CharField(max_length=5),
        ),
    ]