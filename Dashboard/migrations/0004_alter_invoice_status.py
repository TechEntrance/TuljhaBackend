# Generated by Django 5.0.6 on 2024-10-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_organization_contact_person_organization_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]