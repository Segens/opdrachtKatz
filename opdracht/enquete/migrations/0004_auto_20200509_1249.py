# Generated by Django 3.0.6 on 2020-05-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0003_vraag_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vraag',
            name='vraag_score',
        ),
        migrations.AddField(
            model_name='antwoord',
            name='antwoord_score',
            field=models.IntegerField(default=0),
        ),
    ]
