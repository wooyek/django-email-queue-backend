# Generated by Django 2.0.3 on 2018-04-12 14:13

from django.db import migrations, models
import django_email_queue.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_email_queue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuedemailmessage',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Created'), (1, 'Posted'), (2, 'Sending')], default=django_email_queue.models.QueuedEmailMessageStatus(0)),
        ),
    ]