# Generated by Django 4.0.3 on 2022-05-27 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_takeanswer_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='take',
            name='status',
        ),
        migrations.RemoveField(
            model_name='takeanswer',
            name='selected',
        ),
    ]