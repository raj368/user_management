# Generated by Django 3.1 on 2021-02-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountsApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='marital_status',
            field=models.CharField(choices=[('MR', 'Married'), ('SI', 'Single'), ('SE', 'Separated'), ('DV', 'Divorce'), ('OT', 'Others')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='resident_address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('AD', 'Admin'), ('IR', 'Influencer'), ('PR', 'Partner'), ('UR', 'User')], max_length=10, null=True),
        ),
    ]
