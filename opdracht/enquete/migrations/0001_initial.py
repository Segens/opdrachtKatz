# Generated by Django 3.0.6 on 2020-05-08 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vraag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vraag_tekst', models.CharField(max_length=200)),
                ('vraag_type', models.CharField(choices=[('open', 'Open'), ('multichoice', 'Multiple Choice'), ('jaNee', 'Ja/Nee')], max_length=50)),
                ('vraag_score', models.FloatField()),
                ('vraag_meerdere', models.BooleanField(verbose_name='Meerdere juiste antwoorden')),
            ],
            options={
                'verbose_name_plural': 'vragen',
            },
        ),
        migrations.CreateModel(
            name='Antwoord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antwoord_tekst', models.CharField(max_length=200)),
                ('antwoord_juist', models.BooleanField()),
                ('vraag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquete.Vraag')),
            ],
            options={
                'verbose_name_plural': 'antwoorden',
            },
        ),
    ]