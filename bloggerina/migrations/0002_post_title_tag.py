# Generated by Django 5.0.3 on 2024-03-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggerina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]