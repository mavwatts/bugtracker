# Generated by Django 3.1 on 2020-08-29 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker_app', '0005_ticket_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('N', 'New'), ('IP', 'In_progress'), ('D', 'Done'), ('Inv', 'Invalid')], default='N', max_length=3),
        ),
    ]
